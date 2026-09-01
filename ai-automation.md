# AI Automation

AI is most useful as a controlled content assistant. A production workflow should preserve a human decision point before publishing or sending a message.

## Content workflow

```mermaid
flowchart LR
  Brief[Topic or brief] --> Generate[AI tweet generator]
  Generate --> Validate[Length, policy, and duplicate checks]
  Validate --> Rewrite[Optional AI rewrite]
  Rewrite --> Review[Human review]
  Review --> Schedule[Schedule approved content]
  Schedule --> Publish[Publish]
  Publish --> Track[Track engagement]
```

## Comment workflow

```mermaid
flowchart TD
  Discover[Post discovery] --> Context[Context extraction]
  Context --> Draft[AI comment generation]
  Draft --> Review[Review and edit]
  Review --> Publish[Publish approved reply]
```

Validation should check length, links, prohibited content, duplicate phrasing, and account voice. Keep prompts, generated drafts, approvals, and final outcomes in separate audit records so a reviewer can reconstruct what happened.
