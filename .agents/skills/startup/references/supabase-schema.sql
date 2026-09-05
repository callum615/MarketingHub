-- Galway Finance / Claude Code memory schema
-- Run in Supabase SQL editor once per project.

-- Extensions for better retrieval later
create extension if not exists vector;
create extension if not exists pg_trgm;

-- Core identity for multi-project setups
create table if not exists projects (
  id uuid primary key default gen_random_uuid(),
  project_key text not null unique,
  display_name text not null,
  domain text check (domain in ('broker-ops','marketing','compliance','product','general')) default 'general',
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists clients (
  id uuid primary key default gen_random_uuid(),
  project_id uuid not null references projects(id) on delete cascade,
  client_key text not null,
  display_name text not null,
  status text not null default 'active',
  notes text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  unique (project_id, client_key)
);

-- Standing preferences / operating rules (compounding instructions)
create table if not exists preferences (
  id uuid primary key default gen_random_uuid(),
  project_id uuid not null references projects(id) on delete cascade,
  client_id uuid references clients(id) on delete cascade,
  key text not null,
  value text not null,
  priority int not null default 100,
  active boolean not null default true,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create index if not exists preferences_project_idx on preferences(project_id) where active = true;

-- Open and closed decisions
create table if not exists decisions (
  id uuid primary key default gen_random_uuid(),
  project_id uuid not null references projects(id) on delete cascade,
  client_id uuid references clients(id) on delete cascade,
  title text not null,
  decision text not null,
  rationale text,
  status text not null default 'open' check (status in ('open','needs_review','decided','superseded')),
  decided_at timestamptz,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create index if not exists decisions_open_idx on decisions(project_id, status);

-- Active workstreams / initiatives
create table if not exists workstreams (
  id uuid primary key default gen_random_uuid(),
  project_id uuid not null references projects(id) on delete cascade,
  client_id uuid references clients(id) on delete cascade,
  title text not null,
  goal text,
  status text not null default 'active' check (status in ('active','blocked','paused','done')),
  next_action text,
  priority int not null default 100,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create index if not exists workstreams_active_idx on workstreams(project_id, status, priority);

-- Insights learned during sessions
create table if not exists insights (
  id uuid primary key default gen_random_uuid(),
  project_id uuid not null references projects(id) on delete cascade,
  client_id uuid references clients(id) on delete cascade,
  insight text not null,
  importance int not null default 3 check (importance between 1 and 5),
  tags text[] not null default '{}',
  created_at timestamptz not null default now()
);

create index if not exists insights_project_created_idx on insights(project_id, created_at desc);

-- Artifacts produced (reports, pages, campaigns, skills)
create table if not exists artifacts (
  id uuid primary key default gen_random_uuid(),
  project_id uuid not null references projects(id) on delete cascade,
  client_id uuid references clients(id) on delete cascade,
  artifact_type text not null,
  title text not null,
  path_or_url text,
  status text not null default 'active',
  summary text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

-- Session logs written by wrap-up skill
create table if not exists session_logs (
  id uuid primary key default gen_random_uuid(),
  project_id uuid not null references projects(id) on delete cascade,
  client_id uuid references clients(id) on delete cascade,
  started_at timestamptz,
  ended_at timestamptz not null default now(),
  objective text,
  summary text not null,
  outcomes text[] not null default '{}',
  open_loops text[] not null default '{}',
  tools_used text[] not null default '{}',
  raw_notes text,
  embedding vector(1536),
  created_at timestamptz not null default now()
);

create index if not exists session_logs_project_created_idx on session_logs(project_id, created_at desc);
create index if not exists session_logs_summary_trgm_idx on session_logs using gin (summary gin_trgm_ops);

-- Seed default project
insert into projects (project_key, display_name, domain)
values ('galway-finance', 'Galway Finance', 'broker-ops')
on conflict (project_key) do nothing;

-- Helpful startup views
create or replace view v_startup_open_decisions as
select d.*, p.project_key, c.client_key
from decisions d
join projects p on p.id = d.project_id
left join clients c on c.id = d.client_id
where d.status in ('open', 'needs_review')
order by d.updated_at desc;

create or replace view v_startup_active_workstreams as
select w.*, p.project_key, c.client_key
from workstreams w
join projects p on p.id = w.project_id
left join clients c on c.id = w.client_id
where w.status in ('active', 'blocked')
order by w.priority asc, w.updated_at desc;

-- Example startup queries (parameterise project_key)
-- select * from session_logs sl
-- join projects p on p.id = sl.project_id
-- where p.project_key = 'galway-finance'
-- order by sl.created_at desc
-- limit 10;
