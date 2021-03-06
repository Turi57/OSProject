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

First Diagram:
[Taquero Diagram](https://github.com/VictorPeralta/OSProject/blob/master/extra/Taquero_Diagram.png)

Second Diagram:
[Mesero Diagram](https://github.com/VictorPeralta/OSProject/blob/master/extra/Mesero_Diagram.png)


## Contributing

Please read [CONTRIBUTING.md](https://github.com/VictorPeralta/OSProject/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Victor Peralta** - *Initial work* - [VictorPeralta](https://github.com/VictorPeralta)

* **Fernando Cortez** - *Initial work* - [fernandoraulcortezchavez](https://github.com/fernandoraulcortezchavez)

* **Claudia King** - *Initial work* - [mking20](https://github.com/mking20)


See also the list of [contributors](https://github.com/VictorPeralta/OSProject/blob/master/contributors.md) who participated in this project.
