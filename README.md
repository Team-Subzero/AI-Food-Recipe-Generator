# Task Management System - Frontend

React (Vite) frontend for the MERN Task Management System.

## Setup
```bash
npm install
cp .env.example .env     # set VITE_API_URL to your backend URL
npm run dev              # http://localhost:5173
```

## Folder structure
```
src/
  api/          axios instance + service functions
  components/   reusable UI (Navbar, TaskTable, Pagination, modal...)
  context/      AuthContext, ToastContext
  hooks/        useDebounce
  pages/        Login, AdminDashboard, EmployeeDashboard, NotFound
  routes/       ProtectedRoute (role based)
  utils/        constants, validators, helpers
```

## Backend API contract expected
| Method | Endpoint | Body / Query | Response |
|---|---|---|---|
| POST | /auth/login | { email, password, role } | { token, user: { id, name, email, role } } |
| GET | /admin/employees | - | { employees: [{ _id, name, email, createdAt }] } |
| GET | /admin/stats | - | { notStarted, inProgress, completed } |
| GET | /admin/tasks | search, page, limit | { tasks, total, page, totalPages } |
| POST | /admin/tasks | { title, description, assignedTo, priority } | { task } (+ email to employee) |
| GET | /employee/tasks | search, page, limit | { tasks, total, page, totalPages } |
| PATCH | /employee/tasks/:id/status | { status } | { task } (+ email to admin) |

- `role`: `admin` or `employee`
- `status`: `Not Started`, `In Progress`, `Completed`
- `priority`: `High`, `Medium`, `Low`
- Tasks returned to admin must have `assignedTo` populated with `{ name }`.
- Auth: `Authorization: Bearer <token>` header; 401 logs the user out.
