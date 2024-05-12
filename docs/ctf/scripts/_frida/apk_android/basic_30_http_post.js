// function httpPost(targetUrl: string, body: string, onReceive: (response: string) => void = function (response: string) {console.log("response: " + response); }) {
function httpPost(targetUrl, body, onReceive) {
    Java.perform(function () {
        var HttpURLConnection = Java.use("java.net.HttpURLConnection");
        var URL = Java.use("java.net.URL");
        var BufferedReader = Java.use("java.io.BufferedReader");
        var BufferedWriter = Java.use("java.io.BufferedWriter");
        var BufferedOutputStream = Java.use("java.io.BufferedOutputStream");
        var OutputStreamWriter = Java.use("java.io.OutputStreamWriter");
        var StringBuilder = Java.use("java.lang.StringBuilder");
        var InputStreamReader = Java.use("java.io.InputStreamReader");

        var url = URL.$new(Java.use("java.lang.String").$new(targetUrl));
        var conn = url.openConnection();
        conn = Java.cast(conn, HttpURLConnection);
        conn.setRequestMethod("POST");
        conn.setRequestProperty("Content-Type", "application/json");
        conn.setConnectTimeout(5000);
        conn.setReadTimeout(5000);
        conn.setDoInput(true);
        conn.setDoOutput(true);
        conn.setChunkedStreamingMode(0);

        const os = conn.getOutputStream();
        const out = BufferedOutputStream.$new(os);
        const osw = OutputStreamWriter.$new(out, Java.use("java.lang.String").$new("UTF-8"));
        var writer = BufferedWriter.$new(osw);
        let jsonBody = `{"data": "${body}"}`;
       console.log(`Posting: ${jsonBody}`);
        writer.$super.write(Java.use("java.lang.String").$new(jsonBody));
        writer.flush();
        writer.close();
        os.close();

        conn.connect();
        var code = conn.getResponseCode();
       console.log(`Response code: ${code}`);
        var ret = null;
        if (code == 200) {
            var inputStream = conn.getInputStream();
            var buffer = BufferedReader.$new(InputStreamReader.$new(inputStream));
            var sb = StringBuilder.$new();
            var line = null;
            while ((line = buffer.readLine()) != null) {
                sb.append(line);
            }
            var data = sb.toString();
            data = JSON.parse(data)["data"];
            ret = Decrypt(data);
        } else {
            ret = "error: " + code;
        }
        console.log("response: " + ret);
        conn.disconnect();
        onReceive(ret);
    });
}
function onReceive(response)  { console.log("response: " + response); }
httpPost('http://127.0.0.1:8080', "{}", onReceive)
