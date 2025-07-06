# Circle Buffer

## P: Problem
- Inputs: object
- Outputs: 
    - get: returns and removes oldest object

## D: Data Structures
- put: add an object to the buffer
- list to store objects
- need to identify oldest, and next oldest once removed 

## A: Algorithms
- put:
    - use next to identify the next spot to be filled 
    - if the spot is not empty:
        - replace the item with the newest item
    - move next to the next spot 
    - move oldest to the oldest spot 
- get: 
    - check if the buffer is empty
    - if empty return None
    - return and remove the oldest one 
    - update the oldest one 
