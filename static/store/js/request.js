// host ="http://localhost:8000/"

// $.ajax({
//   type: "GET",
//   url: host + "fetch",
//       async: true,
//   success: function(res) {
//     result = JSON.parse(res)
//     console.log(result)
//       dataSet = [];
//       new_arr = [];
//      result.forEach(element => {
//       new_arr[0] = element.s_time
//       new_arr[1] = element.time
//       new_arr[2] = element.aq
//       new_arr[3] = element.ch4
//       new_arr[4] = element.co
//       new_arr[5] = element.h
      
//       dataSet.push(new_arr)
//       console.log(dataSet)
//      });
//   },
//   error: function(){
//   alert("something went wrong")
//   }
// })