| Data packet     |                |
| --------------- | -------------- |
| Start of packet | `d:`           |
| End of packet   | `\n`           |
| End of property | `;`            |
| CPU Temp        | `ct` + integer |
| CPU Usage       | `cu` + integer |
| GPU Temp        | `gt` + integer |
| GPU Usage       | `gu` + integer |
Example data packet: 
```
d:ct42;cu7;gt37;gu69;\n
```
Which means
| Label     | Value |
| --------- | ----- |
| CPU Temp  | 42C   |
| CPU Usage | 7%    |
| GPU Temp  | 37C   |
| GPU Usage | 69%   |