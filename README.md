# bdc

## [c.mygo.fun](https://c.mygo.fun)

分析: bestdori谱面相关资源，并提供复制与下载。

使用 cloudflare worker 代理请求，解决跨域问题。   
纯 HTML 项目。


cloudflare worker.js 代码如下:

```javascript
addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request))
})

async function handleRequest(request) {
  // 目标API的URL，这里作为示例，你应替换成实际的API URL
  let url = new URL(request.url)
  let apiUrl = url.searchParams.get("apiUrl");
  
  // 使用原始请求的方法和体来初始化一个新的请求
  let init = {
    method: request.method,
    headers: request.headers
  }

  // 发送请求到目标API
  const response = await fetch(apiUrl, init)

  // 创建一个新的响应对象来复制原始响应，并添加CORS头部
  let newResponse = new Response(response.body, response)
  newResponse.headers.set("Access-Control-Allow-Origin", "*")
  newResponse.headers.set("Access-Control-Allow-Methods", "GET,HEAD,POST,OPTIONS")
  newResponse.headers.set("Access-Control-Allow-Headers", "*")

  // 返回修改后的响应
  return newResponse
}

```


