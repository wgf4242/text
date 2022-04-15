// 注意驼峰命名 python处是 test_comm
rpc.exports = {
  testComm() {
    var data = Process.enumerateModules()
    send(data)
    recv(function (received_object) {
      var my_data = received_object.my_data
      console.log(my_data)
    }).wait()
    console.log("bye~")
  },
}
