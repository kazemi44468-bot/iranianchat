# IranianChat

پلتفرم جامع چت امن و اختصاصی برای سازمان‌ها، گروه‌ها، جوامع تخصصی و سامانه‌های ارتباطی اختصاصی.

## Vision
IranianChat is designed as a reusable platform core rather than a single-purpose chat website. The architecture supports shared cloud, dedicated deployments and private/on-premise installations.

## Architecture

- **Web:** Next.js + TypeScript
- **API:** NestJS + TypeScript
- **Realtime:** WebSocket gateway
- **Database:** PostgreSQL
- **Cache / presence / rate limiting:** Redis
- **Storage:** S3-compatible object storage
- **Deployment:** Docker-first
- **Architecture:** Modular monolith with explicit service boundaries for future extraction

## Core domains

Identity, users, organizations, tenants, roles, permissions, conversations, messages, groups, channels, files, notifications, presence, search, moderation, audit logs, sessions, devices and security events.

## Security principles

Security is a first-class architectural concern. Tenant isolation, least privilege, secure sessions, auditability, rate limiting, input validation, encrypted transport and safe secret handling are required foundations.

> E2EE is not claimed by the initial scaffold. Production end-to-end encryption requires a complete key-management and multi-device protocol design and must not be simulated with per-message generated keys.

## Initial milestone

Phase 01 establishes the repository, development conventions, environment configuration, Docker services, backend module boundaries and frontend shell. Feature implementation will follow incrementally with tests and security review.
