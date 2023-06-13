## Anaconda 2022 -- TODO and Issues List --

> Bart Gerritsen
> TU Delft, EEMCS

---

1. 	Handling student labs non-terminating executions
	
	- Manifestations:
		- kernel hangs (blacks in the Notebook)
		- execution does not terminate
		- nbgrader times out

	- Causes:
		- Vocareum to hang 
		- `nbgrader` to fail
		- students to have to Interrupt Kernels

	- Solutions:
		- use a safe 'runner' that times out and breaks execution
		- candidate: `module stopit`

	- Actions: 
		- include `stopit` in the DUT Anaconda installation 2022

		