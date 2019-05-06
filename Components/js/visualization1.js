
function data_visualization8() {
    var myChart = echarts.init(document.getElementById('visual-8'));

    var schema = [
        {name: 'Chinese', index: 1, text: '语文'},
        {name: 'Math', index: 2, text: '数学'},
        {name: 'English', index: 3, text: '英语'},
        {name: 'Physics', index: 4, text: '物理'},
        {name: 'Chemical', index: 5, text: '化学'},
        {name: 'Biology', index: 6, text: '生物'},
        {name: 'Policy', index: 7, text: '政治'},
        {name: 'History', index: 8, text: '历史'},
        {name: 'Geography', index: 9, text: '地理'},
        {name: 'Technology', index: 10, text: '技术'}
    ];

    // 数据格式为学科1～学科10，学生id， 班级id
    function retrieveScatterData(data, dimX, dimY){
        var result = [];
        for (var i = 0; i < data.length; i++){
            var item = [data[i][dimX], data[i][dimY]];
            result.push(item)
        }
        return result
    }

    function generateGrid(option){
        var index = 0;
        var sub_name = ['语文', '数学', '英语', '物理', '化学', '生物', '政治', '历史', '地理', '技术'];
        for (var i = 0; i < 2; i ++){
            for (var j = 0; j < 5; j ++){
                option.grid.push({
                    left: 2 + j * (18 + 1.5) + '%',
                    top: 5 + i * (18 + 2) + '%',
                    width: '18%',
                    height: '18%'
                });
                option.brush.xAxisIndex && option.brush.xAxisIndex.push(index);
                option.brush.yAxisIndex && option.brush.yAxisIndex.push(index);
                option.xAxis.push({
                    gridIndex: index,
                    type: 'category',
                    data: []
                });
                option.yAxis.push({
                    name: sub_name[i * 5 + j] + 'T-Score',
                    gridIndex: index,
                    type: 'value'
                });
                option.series.push({
                    type: 'scatter',
                    xAxisIndex: index,
                    yAxisIndex: index,
                    symbolSize: 5,
                    data: []
                });
                index ++;
            }
        }
    }

    option = {
        brush: {
            xAxisIndex: [],
            yAxisIndex: [],
            brushLink: 'all',
            inBrush: {
                opacity: 1
            }
        },
        tooltip: {},
        grid: [],
        xAxis: [],
        yAxis: [],
        parallelAxis: [
            {dim: 0, name: schema[0].text},
            {dim: 1, name: schema[1].text},
            {dim: 2, name: schema[2].text},
            {dim: 3, name: schema[3].text},
            {dim: 4, name: schema[4].text},
            {dim: 5, name: schema[5].text},
            {dim: 6, name: schema[6].text},
            {dim: 7, name: schema[7].text},
            {dim: 8, name: schema[8].text},
            {dim: 9, name: schema[9].text},
        ],
        parallel: {
            bottom: '2%',
            top: '48%',
            left: '5%',
            height: '50%',
            width: '90%',
            parallelAxisDefault: {
                type: 'value',
                name: '成绩一览表',
                nameLocation: 'end',
                nameGap: 20,
                splitNumber: 3,
                nameTextStyle: {
                    fontSize: 14
                },
                axisLine: {
                    lineStyle: {
                        color: '#555'
                    }
                },
                axisTick: {
                    lineStyle: {
                        color: '#555'
                    }
                },
                splitLine: {
                    show: false
                },
                axisLabel: {
                    textStyle: {
                        color: '#555'
                    }
                }
            }
        },
        series: [
            {
                name: 'parallel',
                type: 'parallel',
                smooth: true,
                lineStyle: {
                    normal: {
                        width: 1,
                        opacity: 0.3
                    }
                },
                data: []
            }
        ],
    };

    generateGrid(option);

    myChart.setOption(option);

    $.get('./Dataset/School_Score/4.Score_cla_total_1.json').done(function (data) {
        myChart.setOption({
            xAxis: [{
                data: data.xAxis
            },{
                data: data.xAxis
            },{
                data: data.xAxis
            },{
                data: data.xAxis
            },{
                data: data.xAxis
            },{
                data: data.xAxis
            },{
                data: data.xAxis
            },{
                data: data.xAxis
            },{
                data: data.xAxis
            },{
                data: data.xAxis
            }],
            series: [{
                data: data.score_total
            },{
                data: retrieveScatterData(data.score_total, 11, 0),
            }, {
                data: retrieveScatterData(data.score_total, 11, 1),
            },{
                data: retrieveScatterData(data.score_total, 11, 2),
            }, {
                data: retrieveScatterData(data.score_total, 11, 3),
            },{
                data: retrieveScatterData(data.score_total, 11, 4),
            }, {
                data: retrieveScatterData(data.score_total, 11, 5),
            },{
                data: retrieveScatterData(data.score_total, 11, 6),
            }, {
                data: retrieveScatterData(data.score_total, 11, 7),
            },{
                data: retrieveScatterData(data.score_total, 11, 8),
            }, {
                data: retrieveScatterData(data.score_total, 11, 9),
            }]
        });
    });
}
