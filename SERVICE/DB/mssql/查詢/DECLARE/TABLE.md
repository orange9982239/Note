
> CTE 只能SELECT一次，`DECLARE @tableName TABLE`，在本次查詢可重複使用。
```sql
--定義JSON(用來放範例資料)
DECLARE @json AS VARCHAR(MAX) = '{
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
}'

--定義TABLE @userPosData
DECLARE @userPosData TABLE(
    ID int ,
    Name VARCHAR(max),
    Value VARCHAR(max),
    Type VARCHAR(max)
);

--寫入TABLE @userPosData
INSERT INTO @userPosData (ID,Name,Value,Type)(

    SELECT 
        *
    FROM OPENJSON(@json,'$.Position') 
    WITH (  
        ID int ,
        Name VARCHAR(max),
        Value VARCHAR(max),
        Type VARCHAR(max)
    ) 
)

-- 使用table
SELECT * FROM @userPosData
```