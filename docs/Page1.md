# Page1 Heading

Text here

```eval_rst
+------------+------------+-----------+ 
| Header 1   | Header 2   | Header 3  | 
+============+============+===========+ 
| body row 1 | column 2   | column 3  | 
+------------+------------+-----------+ 
| body row 2 | Cells may span columns.| 
+------------+------------+-----------+ 
```

## Sub-chapter1

Some text

# Heading 2

## Heading2.1

### Heading 2.1.1

### Heading 2.1.2

#### Heading 2.1.2.1

### Heading 2.1.3

# Heading 3

## Heading 3.1

### Heading 3.1.1

### Heading 3.1.2

## Heading 3.2

## Heading 3.3

### Heading 3.3.1

### Heading 3.3.2

#### Heading 3.3.2.1

#### Heading 3.3.2.2

# Heading 4

## Example Table:
```eval_rst
+------------------------+------------+----------+----------+
| Header row, column 1   | Header 2   | Header 3 | Header 4 |
| (header rows optional) |            |          |          |
+========================+============+==========+==========+
| body row 1, column 1   | column 2   | column 3 | column 4 |
+------------------------+------------+----------+----------+
| body row 2             | Cells may span columns.          |
+------------------------+------------+---------------------+
| body row 3             | Cells may  | - Table cells       |
+------------------------+ span rows. | - contain           |
| body row 4             |            | - body elements.    |
+------------------------+------------+---------------------+
```
```eval_rst
+-----------------+------------------+-------------+----------+-------------------------------------------------------------------------------------------------------------------------+
| Tool            | Purpose          | Granularity | Location | Details                                                                                                                 |
+=================+==================+=============+==========+=========================================================================================================================+
| LabVIEW         | Debugging        | N/A         |          | - `Console Viewer: <https://www.ni.com/documentation/en/veristand/latest/manual/viewing-console-output/>`_              |
| Debugging       |                  |             |          | - LabVIEW                                                                                                               |
| Tools           |                  |             |          | - Execution                                                                                                             |
+-----------------+------------------+-------------+------------------------------------------------------------------------------------------------------------------------------------+
```



```eval_rst
+----------------------+---------------------+-------------+------------------------------------------------------------------------------------------------------------------------------------+
| Tool            | Purpose          | Granularity | Location | Details                                                                                                                            |
+======================+=====================+=============+====================================================================================================================================+
| LabVIEW         | Debugging           | N/A         | - Useful before the LabVIEW code has been merged into the custom device framework.                                                 |
| Debugging       |                     |             | - LabVIEW debugging hooks do affect timing.                                                                                        |
| Tools           |                     |             | - Execution highlighting drastically affects VI timing.                                                                            |
+----------------------+---------------------+-------------+------------------------------------------------------------------------------------------------------------------------------------+
| `Console Viewer: <https://www.ni.com/documentation/en/veristand/latest/manual/viewing-console-output/>`_       | Debugging /         | Low         | - Periodic snapshot of utilization, transients and spikes may be missed.                                                           |
|                      | Benchmarking CPU    |             | - Requires the RT Console Viewer daemon.                                                                                           |
+----------------------+---------------------+-------------+------------------------------------------------------------------------------------------------------------------------------------+
| RT Debug String      | Debugging           | N/A         | - Incurs overhead, especially when the console window requires a redraw.                                                           |
+----------------------+---------------------+-------------+------------------------------------------------------------------------------------------------------------------------------------+
| Distributed System   | Benchmarking        | Medium      | - Periodic snapshot of utilization, transients and spikes may be missed.                                                           |
| Manager              | CPU / RAM           |             | - Requires the System State Publisher daemon.                                                                                      |
+----------------------+---------------------+-------------+------------------------------------------------------------------------------------------------------------------------------------+
| System Channels      | Benchmarking timing | High        | - Knowledge of the operator's System Definition is required to make good use of the system channels for benchmarking.              |
+----------------------+---------------------+-------------+------------------------------------------------------------------------------------------------------------------------------------+
| Telemetry            | Benchmarking        | High        | - This is an in-line asynchronous custom device. It logs each CPU core usage, along with RAM and system channels to a TDMS file.   |
| Custom Device        | CPU / RAM / timing  |             |                                                                                                                                    |
+----------------------+---------------------+-------------+------------------------------------------------------------------------------------------------------------------------------------+
| Real-Time Execution  | Debugging /         | Ultra High  | - Execution trace logs contain a vast amount of detailed information. They require a good deal of domain expertise interpret.      |
| Tracing              | Benchmarking        |             | - Using the tool effectively requires starting and stopping the trace directly around the period of interest.                      |
+----------------------+---------------------+-------------+------------------------------------------------------------------------------------------------------------------------------------+
| Additional Debugging | Debugging           |             | - Must request from NI                                                                                                             |
| Options              |                     |             | - Considered a last resort only                                                                                                    |
+----------------------+---------------------+-------------+------------------------------------------------------------------------------------------------------------------------------------+
```

END Page1
