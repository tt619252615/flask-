var myChart = echarts.init(document.getElementById('dashboard'));

// 这是给定的数据，格式为：销售经理，销售代表，客户总数，已购买客户数量，销售额，销售任务额
var rawData = [
  ['王斌', '黄著', 518, 468, 3134352, 3494768],
  ['王斌', '刘旺坚', 1747, 1547, 8150670, 9256901],
  ['王斌', '李文科', 848, 748, 4677846, 5017934],
  ['王斌', '蔡铭浪', 673, 601, 4234075, 4547376],
  ['刘倩', '胡斌彬', 2359, 2059, 9903786, 11351234],
  ['刘倩', '廖舒婷', 479, 429, 2657902, 2975019],
  ['刘倩', '胥玉英', 1162, 1012, 5128837, 4836006],
  ['刘倩', '邵雪梅', 597, 561, 3954075, 4338816],
  ['袁波', '刘俊权', 472, 422, 2290201, 2384432],
  ['袁波', '古旭高', 1338, 1188, 6193413, 6725379],
  ['袁波', '段博艳', 430, 367, 1695026, 1889511],
  ['袁波', '王萍', 1382, 1232, 6736514, 6153310]
];

// 计算销售额相对于销售任务额的百分比，结果四舍五入到小数点后两位
var salesData = rawData.map(function(item) {
  var percentage = (item[4] / item[5]) * 100;
  return [item[1], Math.round(percentage * 100) / 100];
});

var option = {
  series: salesData.map(function(item, idx) {
    return {
      name: '销售任务完成度',
      type: 'gauge',
      center: [(idx % 2) * 50 + 25 + '%', Math.floor(idx / 2) * 40 + 30 + '%'], // 两列的仪表盘
      radius: '30%',
      title: {
        text: item[0],
      },
      detail: {
        formatter: '{value}%',
        fontSize: 14,
      },
      data: [
        {
          value: item[1],
        },
      ],
    };
  }),
};

myChart.setOption(option);
