import json
from pathlib import Path
import uuid
from typing import Any, Callable, Set

# Create a function to submit a support ticket
def submit_support_ticket(email_address: str, description: str) -> str:
    script_dir = Path(__file__).parent # Get the directory of the current script
    ticket_number = str(uuid.uuid4()).replace('-', '')[:6] # Generate a simple ticket number
    file_name = f'ticket-{ticket_number}.txt' # Create a unique file name
    file_path = script_dir / file_name # Create the full file path
    text = f'Support ticket: {ticket_number}\nSubmitted by {email_address}\nDescription: \n{description}' # Prepare the ticket content
    file_path.write_text(text)

    message_json = json.dumps({
        "message": f'Support ticket {ticket_number} submitted. The ticket file is saved as {file_name}.'})
    return message_json

# Define a set of callable functions
user_functions: Set[Callable[..., Any]] = {
    submit_support_ticket  
}


