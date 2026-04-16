## Development Setup and AI Collaboration

### System Setup

Our application is built using **Flask** with **SQLAlchemy** and runs in a containerized environment using **Docker Compose**.

The system consists of:
- **web container** → Flask application
- **db container** → PostgreSQL database

Development is carried out in:
- Local Docker environments
- GitHub Codespaces (container-based)

Tests are executed using:
```bash
docker compose exec web python -m pytest
````



### Team Roles

#### Human Members
- Design system architecture
- Implement and integrate features
- Review and test all code before merging
- Manage GitHub branches and pull requests

#### AI Assistance
- Assists with debugging errors (e.g., Docker, database issues)
- Explains concepts when needed
- Suggests improvements or alternative implementations
- Help generate tests when needed

AI is used as a development assistant, while all final decisions remain with the team.


### Ensuring Correct Direction

To ensure the project stays aligned:

- The team agrees on architecture and design decisions before implementation

- GitHub is used for:
  - version control
  - pull requests
  - tracking changes

- Code reviews ensure consistency and correctness
- Testing (`pytest`) is used to validate functionality

