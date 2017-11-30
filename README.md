# Tacos Shop Operating System

This application is for a Taco Shop (Tacos Franc). 
The project is going to have three main parts:

* Scheduling algorithms to manage orders:
```
  Tacos, Tostadas, Tortas, Quesadillas, Mulitas --> "Ordenes": Asada, Adobada, Suadero, Lengua, Cabeza.
  "Ingredientes": Cebolla, Cilantro, Salsa, Frijoles y Guacamole.
  "Threads": Taqueros, Tortillera, Meseros.
```
* Meta information about waiting times, resources status, maintenance, available waiters, available tables, standing eating spaces.
* Realtime visualizations about metadata.

### Requisites
* Each "taquero" has his own fairy of dreams(tortillera).
* Five Graphs, for example:
```
  Type Time (Taco, Quesadilla)
  Meat Time.
  Order Size Time.
  Cycles.
  Priorities.
```
* Only three "taqueros" will do different things to complete each order.
* Unlimited ingredients, but it is necessary to refill from the available. If it is sequential refill, then is necessary to do:
```
  thread.sleep/time.sleep. 
```
  Another option is to refill in parallel (another thread).
* The initial ingredients value will be 500. Each "taco" needs a unit per ingredient.
* The process will be:
```
  Read from team Queue (SQS)
  Process the message (core of the project)
  Write in Response Queue (SQS)
  Delete from Team Queue (SQS) using receipt  
```
* The order might have 1 to 10 parts (sub orders)
* The team is capable to describe the scheduling algorithm and it needs to be described in a diagram (README).
* According to the algorithm, it should be modified in the configuration and compared the effect. E.g. 
```
Atender a dos clientes al mismo tiempo vs atender a 5 clientes al mismo tiempo.
```
* The read queue is : https://sqs.us-east-1.amazonaws.com/292274580527/cc406_team4 and the write one is: https://sqs.us-east-1.amazonaws.com/292274580527/cc406_response4 (Where 4 is the number team. Each team has its own queue to read and write.)
* JSON format:
```
{  
   "datetime":"2017-01-01 23:23:23",
   "request_id":"123-123-123",
   "orden":[  
      {  
         "part_id":"123-111",
         "type":"taco",
         "meat":"asada",
         "quantity":3,
         "ingredients":[  
            "cebolla",
            "salsa"
         ]
      },
      {  
         "part_id":"123-222",
         "type":"mulita",
         "meat":"asada",
         "quantity":1,
         "ingredients":[  

         ]
      }
   ],
   "answer":{  
      "start_time":"",
      "end_date":"",
      "steps":[  
         {  
            "step":1,
            "state":"running",
            "action":"working on orden",
            "part_id":"123-123",
            "startTime":"",
            "endTime":""
         },
         {  
            "step":2,
            "state":"suspend",
            "action":"waiting for cheese",
            "part_id":"123-222",
            "start_time":"",
            "end_date":""
         },
         {  
            "step":3,
            "state":"running",
            "action":"working on orden",
            "part_id":"123-222",
            "start_time":"",
            "end_date":""
         }
      ]
   }
}
```
To run the program it is necessary to install some librabries:

* You need to install some libraries in python to see the graphs of the project.

```
import matplotlib.pyplot as plt
```

### Installing

In the terminal of linux you can write the next example:

```
sudo apt-get install python-matplotlib
```
Another libray that will be needed is goignt to be installed like this:
```
sudo apt-get install python-tabulate
```
Moreover, is necessary to have boto3:
```
sudo apt-get install python-boto3
```
And that's it, now you can see how the real time graphs of the project interact.

## Diagrams

Mesero Diagram (https://www.draw.io/?lightbox=1&highlight=0000ff&layers=1&nav=1&title=RRS#R7Vpbc5s6EP41PPYMSIDxY2wn5zy0nU6TmXPyKBsZ1AJyhYjt%2FvojgbjKTlzHBnvizCSB1QVpv%2F12VwsGnMabvxlahV%2BojyMDmP7GgDMDAAuMPPFPSraFxIWwEASM%2BKpTLXgkv7ESmkqaER%2BnrY6c0oiTVVu4oEmCF7wlQ4zRdbvbkkbtp65QgDXB4wJFuvRf4vOwkHpgVMv%2FwSQIyydb7rhomaPFz4DRLFHPMwBc5j9Fc4zKudRG0xD5dN0QwXsDThmlvLiKN1McSd2WaivGPexprdbNcMIPGQAWlocWwEamj%2BDcXX6CaoqUb0tlYF%2FoRt1SxkMa0ARF97V0km8YyylNcRfyOBKXlrjEG8L%2Fk%2BK%2FHHX3XLYknG0bTfL2WU3wA3O%2BVUaBMk6FqH7uZ0pXao4lTfgDikkkreyJxMJigPkVr8Xf7zRGiehSbEbuYK%2BCyg3TjC3wHq2UNohYgPk%2BzdX4CV5gGmOxJTGI4Qhx8tJeAFIGGlT9apDEhcLpQMzUnC8oytRTHsVKuQZkDZPU3jokHD%2BuUL7pteBxG7oDlIvYQqHkmJWuXzDjePO6tnUlqQEQ2sWQdYN1iiphg3DQPIMaSx91WtO3GobfsPWqqTL8vO3yTB%2F0Yfr50DvG0LbRYUVJwtPGzN%2BkoDYWp4wW2yrstH3dG%2F1dp2MuxQJq46l2cqQ9uTdXeqQ9OUO5UqC5UmMKjMnD%2FYakHCdyc9ncmEJjApmPE5mjPOh%2BNqTxPEtP4mNP4VQBaNn9eKT5WMt0dCfrnsXJDssJ62o5AYaihA1ubmwHHOYBmNmDpYR237mMeRW5zCGgwfFgwcfUos%2BdT%2BfIR2KqzzgJMnTxsaY8P6pYAxxTCzbeSI81zllizc1z7U3WLzXaQJ0DX3CKGc2f%2FkJSJPdHgoyITWNxTWUeptOiheJFUAOM7RY1djDDci2dGuc569qamr9STYtis7ytKoZT8hvN8w5Ss%2BqMJno7E8OZyaKAMPK0sHc5AEUkEAqcRXgpp5IaJAsU3SkxlwSYpAIakgRPORs%2B2b1BYtudE6Spp8ZwR%2FkBnAWSUT8h%2B4Qe6bXofypv5RwSsr13uqvdBQPbaZsHKE9J5RTFotSoGvr9hYyWcbyzvGDfKrXH2gsYLC8vl9dM8dIiwXtiZHV1%2BZ3lDZjf2XY%2FHvO6DjnQ6yG%2FO65gO24Xokp%2Furdg2%2BkPPfPV%2FqATzv%2B0f6eAfIaKsKexf4aY0SkqSo2K3yf0KxN5r%2B7lLzC3te02UtZ4R3K7K5M6S3JrX18mdSruv7d2sY%2BInURodFgidBLOjP%2BcM%2Fq5%2Fwo4U9Xbh%2BFMTy%2BrLo8z7y7S7uYMHLWP%2B2Uw6oMztl5EeZMzesH4AjkDzXFbqWBQzujh%2FAMWUaDXNvRK10MUUWw9WtwgEeofEBJHd0bPOP3wmFjOgLVGR%2F9k7CNiYnfCiTUaEhNww2QHJrvek%2FSHCdQwMYAb5QCIbbgBzzft%2FsrkB7uT8k1VeS9GzggKGIrLUWIFzYFvYptyRn%2FiKY0oE5KEJjLtXpIo6ogUWkLgaNiBfekbFUAto%2Fzz45D4MiPspvR9Qd7xjBrgFbpNxK0jIBe39cfVRapdf8EO7%2F8H)

## Contributing

Please read [CONTRIBUTING.md](https://github.com/VictorPeralta/OSProject/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Victor Peralta** - *Initial work* - [VictorPeralta](https://github.com/VictorPeralta)

* **Fernando Cortez** - *Initial work* - [fernandoraulcortezchavez](https://github.com/fernandoraulcortezchavez)

* **Claudia King** - *Initial work* - [mking20](https://github.com/mking20)


See also the list of [contributors](https://github.com/VictorPeralta/OSProject/blob/master/contributors.md) who participated in this project.
