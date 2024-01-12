# PLM system with SQLite and Python
 
## This code includes the following features:

### Database Management:
- Creates a SQLite database.
- Defines a table specifically for storing PCB design files.
- Offers basic CRUD (Create, Read, Update, Delete) operations to manage the data within the database.

### Issue Tracking and Management:
- Enables users to create issues to track bugs, enhancements, and other tasks.
- Allows for issue categorization (e.g., bug, enhancement).
- Supports prioritization of issues based on importance.
- Facilitates assignment of issues to specific team members.

### Version Control Integration:
- Integrates basic version control features.
- Allows users to check-in and check-out PCB design files, similar to Git functionality.
- Maintains version history to track changes over time, enabling review of file modifications.

### Project Dashboard and Reporting:

- A dashboard for an overview of all PCB design projects, including their current status, recent updates, and pending tasks.
- Reporting features that allow users to generate status reports and performance metrics.

### Revision Locking and Unlocking:

- A feature to lock revisions of PCB designs, preventing further changes, akin to Perforce's file locking mechanism.

### Workflow Automation:

- An automated workflows for common processes, such as automatic notifications when a PCB design is updated or when an issue is resolved.

### Branching and Merging for Designs:

- Similar to Git, we have the concept of branching and merging for PCB designs. 
- This allows for experimenting with different design variations without affecting the main design.

### REST API for Integration:

- RESTful API to allow integration with other tools and platforms, enhancing the interoperability of your system.