| Data packet     |                |
| --------------- | -------------- |
| CPU Temp        | `ct ` + integer |
| CPU Usage       | `cu ` + integer |
| GPU Temp        | `gt ` + integer |
| GPU Usage       | `gu ` + integer |
| Memory Used     | `mu ` + integer |
| Memory Total*   | `mt ` + integer |

Example data packet: 
```
ct 42
cu 7
gt 37
gu 69
mt 16384
mu 7667
```
Which means
| Label     | Value |
| --------- | ----- |
| CPU Temp  | 42C   |
| CPU Usage | 7%    |
| GPU Temp  | 37C   |
| GPU Usage | 69%   |

\* memory total should not be sent more than once