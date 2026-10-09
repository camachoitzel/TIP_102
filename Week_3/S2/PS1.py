"""
At a cultural festival, multiple performances are scheduled on a single stage. However, due to last-minute changes, some performances need to be rescheduled or canceled. The festival organizers use a stack to manage these changes efficiently.

You are given a list changes of strings where each string represents a change action. The actions can be:

"Schedule X": Schedule a performance with ID X on the stage.
"Cancel": Cancel the most recently scheduled performance that hasn't been canceled yet.
"Reschedule": Reschedule the most recently canceled performance to be the next on stage.
Return a list of performance IDs that remain scheduled on the stage after all changes have been applied.

def manage_stage_changes(changes):
    pass
Example Usage:

print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) 
Example Output:

["A", "C", "B", "D"]
[]
["Z"]

UNDERSTAND:
Input: A list of strings
Output: A list of strings
Edge Cases: empty list, letter cases, all cancel 

PLAN:
- check if list is empty
- create 2 stacks one for scheduled and one for cancelled
-create empty list for final schedule
-loop though list
    - add to sheduled stack if word is schedule 
    - if word is cancel
        -pop from scheduled stack if word is cancel
        - add popped schedule to cancelled stack
    - if reschedule
        - pop from cancelled stack and add to schedule stack
    - once you reach the end of the list
     - pop from scheduled stack and add to final schedule list
    

"""
def manage_stage_changes(changes):
    if not changes:
        return []

    scheduled_stack = []
    cancelled_stack = []

    for change in changes:
        if change.startswith("Schedule"):
            id = change.split()[1]
            scheduled_stack.append(id)
        elif change == "Cancel":
            if scheduled_stack:
                cancelled_id = scheduled_stack.pop()
                cancelled_stack.append(cancelled_id)
        elif change == "Reschedule":
            if cancelled_stack:
                reschedule_id = cancelled_stack.pop()
                scheduled_stack.append(reschedule_id)

    return scheduled_stack

    