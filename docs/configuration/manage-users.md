---
title: Manage Users
icon: material/account-group
---

# Manage Users

!!! note "Requires User System enabled"
    This page is only visible when **Enable User System** is turned on under [UI Settings](ui-settings.md#system-behavior).

Manage Users is accessible from the sidebar and allows you to add/delete users, change your password, manage API tokens, and configure SSO/OIDC.

---

## User list

Displays all current users with their username, role, and an SSO badge if the account was created via Single Sign-On. Admins can be deleted only if there is more than one admin account.

---

## Add New User

| Field | Description |
|---|---|
| **Username** | The login username for the new account |
| **Password** | Initial password |
| **Role** | `User`, `Requester`, or `Admin` |

---

## Change My Password

Available for local accounts only. SSO users manage their password through their identity provider.

---

## API Token

Used to access cli_debrid endpoints externally (e.g. OpenClaw, homepage widgets).

- Append `?token=<your-token>` to API requests
- Use **Regenerate** to invalidate the old token and issue a new one immediately

---

## SSO / OIDC Configuration

| Setting | Description |
|---|---|
| **Enable SSO** | Enable Single Sign-On login |
| **Provider** | Authentik, Authelia, or Generic OIDC |
| **Discovery URL** | OIDC discovery endpoint, e.g. `https://auth.example.com/application/o/cli-debrid/.well-known/openid-configuration` |
| **Client ID** | OAuth2 client ID (e.g. `cli-debrid`) |
| **Client Secret** | OAuth2 client secret. Leave blank for a public client. |
| **Default Role for New Users** | Role assigned to new SSO users — `User`, `Requester`, or `Admin` |
| **Auto-provision New Users** | Automatically create an account on first SSO login |
| **Disable Local Login** | Hide the username/password form — SSO only. Ensure SSO works correctly before enabling. |
| **Public Base URL** | Override the base URL used for the OIDC callback. Required if cli_debrid is behind a reverse proxy. Leave blank to auto-detect. |
| **Callback URI** | Read-only. Copy this value into your identity provider (e.g. Authentik application redirect URIs). |

!!! warning "Disable Local Login"
    Only enable **Disable Local Login** after confirming SSO works correctly. If SSO breaks, you will be locked out of your instance.

---

## Emergency reset (locked out)

If you are locked out of your instance and cannot access the UI, use the `reset_admin.sh` script from inside the container.

**Reset all users and create a fresh admin/admin account:**

```bash
./reset_admin.sh --reset-all
```

**Reset all admin account passwords to `admin` without removing other users:**

```bash
./reset_admin.sh --reset-admin-password
```

**How to run it (Docker):**

1. Open a terminal into the container:
   ```bash
   docker exec -it <container_name> bash
   ```
2. Navigate to the app directory (usually `/app`):
   ```bash
   cd /app
   ```
3. Run the script with one of the flags above

!!! warning "Destructive action"
    `--reset-all` deletes **all** users permanently. Use `--reset-admin-password` if you only need to regain access without losing other accounts.
