---
tags: [skill-creator]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

We're planning Q1 for Tallybook, a small invoicing web app for freelancers (about 2,000 active users, two developers). What it does today: create invoices and send them as PDFs, a client list, payment status tracking, and recurring invoices.

Backlog candidates:
1. CSV export of invoices (accountants keep asking for it at tax time)
2. A plugin system so users can build their own integrations
3. Real-time collaboration so freelancers and their accountants can edit invoices together
4. A custom report builder with drag-and-drop charts on any field
5. Fix: Ctrl+S saves the draft twice

Also, recurring invoices gets a lot of bug reports and only about 4% of users use it. Should we keep it?

Which of these should we actually do?
