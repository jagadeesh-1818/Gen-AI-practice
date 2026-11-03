from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
The standard working schedule is Monday to Friday, from 9:30 AM to 6:30 PM.
Employees must complete eight working hours daily, excluding a one-hour lunch break.

The company follows a hybrid working model. Employees are required to work from the office at least three days per week. The remaining two days can be worked remotely with manager approval.
Employees arriving more than 15 minutes late must record the reason in the attendance management system.
Three consecutive unapproved absences may result in disciplinary action.
Employees working on weekends to meet project deadlines are eligible for compensatory leave, provided their manager approves the request in advance.
"""

splitter=  RecursiveCharacterTextSplitter(
    chunk_size= 40,
    chunk_overlap = 0
)

chunks = splitter.split_text(text)

print(len(chunks))

print(chunks)