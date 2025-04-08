# 解開JSON => 表

## EXAMPLE
### JSON OBJECT
* SQL
    ```sql
        SELECT 
            *
        FROM OPENJSON(
            '{
                "Position": [
                    {
                        "ID": 7,
                        "Name": "招生名額別(進修學士)",
                        "Value": "0",
                        "Type": 1
                    },
                    {
                        "ID": 8,
                        "Name": "繳費身分(進修學士)",
                        "Value": "1",
                        "Type": 3
                    },
                    {
                        "ID": 9,
                        "Name": "加分身分(進修學士)",
                        "Value": "0",
                        "Type": 2
                    }
                ]
            }',
            '$.Position'
        ) 
        WITH (  
            ID int ,
            Name VARCHAR(max),
            Value VARCHAR(max),
            Type VARCHAR(max)
        ) AS Position
    ```
* RESULT

    |ID	|Name                   |Value	|Type   |
    |---|---                    |---    |---    |
    |7	|招生名額別(進修學士)       |0	    |1  |
    |8	|繳費身分(進修學士)         |1      |3  |
    |9	|加分身分(進修學士)         |0      |2  |

### JSON Array
* SQL
    ```sql
    SELECT 
        *
    FROM OPENJSON('[
        {"id":0,"value":"一般"},
        {"id":1,"value":"低收"}
    ]')
    WITH (
        id VARCHAR(max),
        value VARCHAR(max)
    ) AS pos
    ```
* RESULT
    |id|value|
    |---|---|
    |0|一般|
    |1|低收|

### JSON CTE
> JSON讀進CTE TABLE，JOIN 起來。
* SQL
    ```sql
    -- JSON 定義
    ;WITH 
        CTE_userPosData AS(
            -- JSON OBJECT => TABLE
            SELECT 
                *
            FROM OPENJSON(
                '{
                    "Position": [
                        {
                            "ID": 7,
                            "Name": "招生名額別(進修學士)",
                            "Value": "0",
                            "Type": 1
                        },
                        {
                            "ID": 8,
                            "Name": "繳費身分(進修學士)",
                            "Value": "1",
                            "Type": 3
                        },
                        {
                            "ID": 9,
                            "Name": "加分身分(進修學士)",
                            "Value": "0",
                            "Type": 2
                        }
                    ]
                }',
                '$.Position'
            ) 
            WITH (  
                ID int ,
                Name VARCHAR(max),
                Value VARCHAR(max),
                Type VARCHAR(max)
            ) AS userPosData
        ),
        CTE_pos AS(
            -- JSON ARRAY => TABLE
            SELECT 
                *
            FROM OPENJSON('[
                {"id":0,"value":"一般"},
                {"id":1,"value":"低收"}
            ]')
            WITH (
                id VARCHAR(max),
                value VARCHAR(max)
            ) AS pos
        )
    SELECT
        pos_name = A.Name,
        pos_type = A.Type,
        pos_value = A.value,
        pos_valueName = B.value
    FROM 
        CTE_userPosData A 
        INNER JOIN CTE_Pos B ON
            A.VALUE = B.id
    ```
* RESULT
    |pos_name	           |pos_type	|pos_value	|pos_valueName|
    |---                    |---        |---        |---            |
    |招生名額別(進修學士)	|    1	    |    0	    |    一般|
    |加分身分(進修學士)	   |    2	    |    0	    |    一般|
    |繳費身分(進修學士)	   |    3	    |    1	    |    低收|