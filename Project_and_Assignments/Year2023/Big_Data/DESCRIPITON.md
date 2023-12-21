# BIG DATA SYSTEM DESIGN

### Design big data system on specified topic
• Problem statement

• System design diagram (Data flow, components/software used, etc.)

• Design justification (Why you design the system this way?)

• Benefits of this design choice

• Other suggestion

### TOPIC: KEEPING A PROMISES
Stark Industry is planning to distribute a small model of Arc Reactor for household use.
Chairperson promises to the users with 24/7 availability. So, they have to monitor for the remaining lifetime of the reactor and send a new one for replacement before failure occurred. In initial phase, 1000 unit of the reactor have been tested and the result are stored on the main database of the company. In upcoming public release of the reactor, the marketing team expected over 1000000 unit will be sold. You, as the maintenance team, decides to use survival analysis to predicts remaining lifetime of the reactor. They have to do this daily to ensure minimum failure. Arc reactor comes with the feature to send their
current condition to the headquarter. So, they will have to design a new system to aggregate the data and predicts the remaining lifetime of each unit.

In summary, you will have to design a maintenance system that:
• Capable of aggregating data from over 1000000 units.
• Predicts remaining lifetime of each unit using Survival Analysis. Predicts daily.
• Update the survival analysis parameters from collected data every week.
• Generate the report of the maintenance process to the chairperson every week.
