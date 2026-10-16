# Wilson et al. 2017: Good enough practices in scientific computing

- Source: `wilson2017good`, local PDF `papers/pdf/wilson2017good.pdf`
- Version: PLoS Computational Biology 13(6): e1005510, 2017, open access

### E1

- Location: Introduction
- Quote: "a minimum set of tools and techniques that we believe every researcher can and should consider adopting"
- Key point: The paper gives a minimum set of practices that every researcher can and should consider adopting.

### E2

- Location: Introduction
- Quote: "the collaborator every researcher cares about most: their future self" / "yourself from 3 months ago doesn’t answer email"
- Key point: The main beneficiary of these practices is your future self: you from three months ago don't answer email.

### E3

- Location: Box 1, data management
- Quote: "Save the raw data." / "Ensure that raw data are backed up in more than one location." / "Record all the steps used to process data."
- Key point: Save the raw data; back up raw data in more than one location; record every step used to process the data.

### E4

- Location: Box 1, data management and collaboration
- Quote: "Submit data to a reputable DOI-issuing repository so that others can access and cite it." / "Make the license explicit."
- Key point: Submit data to a reputable repository that issues DOIs (Digital Object Identifiers) so others can access and cite it; make the license explicit.

### E5

- Location: Introduction
- Quote: "Many of our recommendations are for the benefit of the collaborator every researcher cares about most: their future self (as the joke goes, yourself from 3 months ago doesn’t answer email"
- Key point: The main beneficiary of these practices is your future self: you from three months ago don't answer email.

### E6

- Location: Project organization, 4a
- Quote: "Put each project in its own directory, which is named after the project (4a). [...] As a rule of thumb, divide work into projects based on the overlap in data and code files."
- Key point: Put each project in its own directory named after the project; divide work into projects based on the overlap in data and code.

### E7

- Location: Project organization, 4b–4d
- Quote: "Put text documents associated with the project in the doc directory (4b). This includes files for manuscripts, documentation for source code, and/or an electronic lab notebook recording your experiments."
- Key point: Put text documents for the project (manuscripts, code documentation, an electronic lab notebook recording your experiments) in the doc directory.

### E8

- Location: Project organization, 4c
- Quote: "Put raw data and metadata in a data directory and files generated during cleanup and analysis in a results directory (4c)"
- Key point: Put raw data and metadata in a data directory, and files generated during cleanup and analysis in a results directory.

### E9

- Location: Data management, 1a
- Quote: "Save the raw data (1a). [...] Consider changing file permissions to read-only or using spreadsheet protection features so that it is harder to damage raw data by accident or to hand edit it in a moment of weakness."
- Key point: Save the raw data; consider making it read-only so it is harder to damage by accident or hand-edit in a moment of weakness.

### E10

- Location: Data management, 1b
- Quote: "Ensure that raw data are backed up in more than one location (1b)."
- Key point: Back up raw data in more than one location.

### E11

- Location: Collaboration, 3a
- Quote: "Create an overview of your project (3a). Have a short file in the project’s home directory that explains the purpose of the project."
- Key point: Put a short overview file (usually called README) in the project's home directory explaining the project's purpose.

### E12

- Location: Collaboration, 3b
- Quote: "Create a shared "to-do" list (3b). This can be a plain text file called something like notes.txt or todo.txt"
- Key point: Create a to-do list; a plain text file is enough.

### E13

- Location: Project organization, 4f
- Quote: "Name all files to reflect their content or function (4f). [...] Do not use sequential numbers (e.g., result1.csv, result2.csv) or a location in a final manuscript (e.g., fig_3_a.png), since those numbers will almost certainly change as the project evolves."
- Key point: Name files to reflect their content or function; don't use sequential numbers or positions in the manuscript, since those numbers will almost certainly change.

### E14

- Location: Keeping track of changes, 5b
- Quote: "Keep changes small (5b). [...] As a rule of thumb, a good size for a single change is a group of edits that you could imagine wanting to undo in one step at some point in the future."
- Key point: Keep changes small; a good size is a group of edits you could imagine wanting to undo in one step.

### E15

- Location: Keeping track of changes, 5f
- Quote: "Add a file called CHANGELOG.txt to the project’s docs subfolder (5f), and make dated notes about changes to the project in this file in reverse chronological order (i.e., most recent first). This file is the equivalent of a lab notebook"
- Key point: Keep a changelog file with dated notes in reverse chronological order; it is the equivalent of a lab notebook.

### E16

- Location: Keeping track of changes, benefits of version control
- Quote: "Instead of relying on users to choose sensible names for backup copies, the version control system timestamps all saved changes automatically."
- Key point: Version control timestamps every saved change automatically, instead of relying on people to give backup copies sensible names.

### E17

- Location: Keeping track of changes, What not to put under version control
- Quote: "Keeping intermediate data files and other results under version control is also not necessary if you can regenerate them from raw data and software."
- Key point: Intermediate data and results need not be under version control if they can be regenerated from the raw data and software.

### E18

- Location: Project organization, the notes after Box 3
- Quote: "The doc directory contains 2 text files written in Markdown, 1 containing a running lab notebook describing various ideas for the project and how these were implemented, and the other containing a running draft of a manuscript describing the project findings."
- Key point: The example project's doc directory holds two running files: a lab notebook and a manuscript draft.

### E19

- Location: Project organization, 4c
- Quote: "Intermediate files such as cleaned data, statistical tables, and final publication-ready figures or tables should be separated clearly by file-naming conventions or placed into different subdirectories; those belonging to different papers or other publications should be grouped together."
- Key point: Within results, intermediate files and publication-ready figures and tables are separated by type, and results belonging to different papers are grouped separately.

### E20

- Location: Data management, Save the raw data (1a)
- Quote: "It is tempting to overwrite raw data files with cleaned-up versions, but faithful retention is essential for rerunning analyses from start to finish, for recovery from analytical mishaps, and for experimenting without fear."
- Key point: It is tempting to overwrite raw data with cleaned versions, but keeping the raw data intact is essential for rerunning analyses from start to finish, recovering from analytical mishaps, and experimenting without fear.

### E21

- Location: Data management, Save the raw data (1a)
- Quote: "In that case, record the exact procedure used to obtain the raw data, as well as any other pertinent information, such as an official version number or the date of download."
- Key point: For large public databases that are impractical to store locally, record the exact procedure used to obtain the raw data, plus details such as the official version number or download date.
