# Console
1. 打開chrome
2. F12召喚出console
3. 允許貼上
    > * 若貼上時遇到以下訊息，輸入`allow pasting`就能允許貼上
    > * Warning: Don’t paste code into the DevTools Console that you don’t understand or haven’t reviewed yourself. This could allow attackers to steal your identity or take control of your computer. Please type ‘allow pasting’ below and hit Enter to allow pasting.
4. 快樂使用JS
    ```js
    console.log("Hello World");
    ```

## 

## 透過JS做出C#能用的JSON
* chrome console => `JSON.stringify(#Jarray#).replaceAll("\"","\\\"")`
* js 物件/陣列 JSON.stringify() 壓製成string，再用replaceAll代換"=>\"則為C#中可用格式。

``` js
JSON.stringify([
    {
        "id":"A123123123",
        "name":"王曉明",
        "enroitems":[
            {
                "id":"1",
                "name":"資管碩班",
                "price":"1200"
            },
            {
                "id":"1",
                "name":"資管博班",
                "price":"1500"
            }
        ]
    },
    {
        "id":"B123123123",
        "name":"王曉明2",
        "enroitems":[
            {
                "id":"1",
                "name":"資工碩班",
                "price":"1200"
            },
            {
                "id":"1",
                "name":"資工博班",
                "price":"1500"
            }
        ]
    }
]).replaceAll("\"","\\\"")

// '[{\\"id\\":\\"A123123123\\",\\"name\\":\\"王曉明\\",\\"enroitems\\":[{\\"id\\":\\"1\\",\\"name\\":\\"資管碩班\\",\\"price\\":\\"1200\\"},{\\"id\\":\\"1\\",\\"name\\":\\"資管博班\\",\\"price\\":\\"1500\\"}]},{\\"id\\":\\"B123123123\\",\\"name\\":\\"王曉明2\\",\\"enroitems\\":[{\\"id\\":\\"1\\",\\"name\\":\\"資工碩班\\",\\"price\\":\\"1200\\"},{\\"id\\":\\"1\\",\\"name\\":\\"資工博班\\",\\"price\\":\\"1500\\"}]}]'
```