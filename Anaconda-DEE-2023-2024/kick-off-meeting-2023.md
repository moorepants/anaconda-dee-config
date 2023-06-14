# Anaconda DEE Config 2023-2024 

> Kick-off meeting June 13, 2023

> Jason K. Moore (JM, 3Me)   
> Kevin Geboers (KG, ICT-WPS)   
> Ciprian Ionescu (CI, EWI)   
> Bart Gerritsen (BG, EWI)

-----

> DEE = Digital Exam Environment

-----

## Goal

1. discussing the __2023-2024 DEE configuration__ update process
2. finding a successor for BG, who will be away after this update cycle.

## Discussion

Open discussion on the future of:

1. the DEE and the way we set it up now
2. the present use of __Vocareum__ and the impediments experienced
3. alternatives, most profoundly: 

    - using a __JupyterHub__ instead of Vocareum, and;
    - using other tools than the __NotebookApp__

### 1. DEE setup

Vocareum contains a proprietary implementation of a JupyterHub, the use of which is now contracted on a limited commercial contract. Vocareum is used for lab assignments campus-wide, but does not comply with the Digital Exam Environment standards and can therefor not be used for exams. Exams are held in the DEE, using the NotebookApp running Python and friends as offered in the Anaconda installation.

The choice with respect to organizing the DEE, is:

- maintaining an single, expanded DEE in which the needs/desires of every faculty user for every course is covered

- splitting into multiple environments, easier to tweak, but coming with a need for _environment management_ by ICT-WPS

As or now, we continue opting for implementing a single, expanded `base` environment for everyone in the DEE, following the procedure we developed over recent years.


### 2. Vocareum

Vocareum is still in a restricted, try-out setup, running largely limited and obsolete tools and versions. Request for upgrades and expansions have been unfruitful so far. This leads to serious problems in the Exam preparations across courses using it. 

Main problem:

- It is unclear if this can be repaired before the next academic year

- We need some final decision making here, in view of our planning


### 3. JupyterHub and other tools

Without dwelling on technical details:

- the use of TU Delft JupyterHub was discussed as a viable alternative for Vocareum's proprietary JupyterHub implementation

- along with this, we discussed the use of JupyterLab, VSCode and other IDE's for students and staff during courses _and_ during exams

Main considerations;

- using a JupyterHub is the only feasible-and-affordable way to streamline (the increasing demand for) auto-graded digital exams on a massive scale, obeying the Delft University Digital Exam Environment standards, without confusing students due to differences in their working environments within and across their courses

- using a JupyterHub enables a seamless and affordable way to cooperate in (the increasing demand for) cross-university labs, assignments and possibly also exams, without compromising standards such as the Digital Exam Environment Standards

- using a JupyterHub opens up a natural migration path for scaling up and/or outsourcing trustworthy exam tools to SURF. SURF could operate the tools, while account end exam management remains at the university

- a business case could be worked out as a further underpinning of the above

## Further steps

1. booting up and taking usual further steps to draft the DEE's `base` environment like we did in the past years (BG + KG)

2. setting up a side track to further investigate (possibly: prototype) a campus-wide JupyterHub for assignments _and_ exams (KG+JM+BG+CI). A business case may be part of the activities. The base case will compare a possible Vocareum update with the migration towards a JupyterHub solution

3. ICT-WPS (KG) to investigate the possibilities for a project to guide the prototyping of a JupyterHub solution, 3mE (JM) to bring in the (halted) proposal for a JupyterHub plus related materials, as a kick off for this effort, EWI (BG+CI) to investigate the possibilities for EWI-students to serve as a TA in this

## Future

At the start of the meeting, JM was found willing to take over the efforts of BG, who will be leaving the DUT within a couple of months. As a first step, BG and JK will discuss the handing over of the existing `Anaconda-DEE-config` repo on `Gitlab`. 
