import React from 'react';
import Ec from './Ec'

export default function(){
    // 学生的历次考试排名的变化，其中需要包含置信区间
    const xlabel = ['2016学年度第一学期期中考试', '2016学年度第一学期考查课总评', '2016学年度第一学期期末考试', '2016学年度第一学期期末总评', '2016学年度第二学期期中考试', '2016学年度第二学期考查课总评', '2016学年度第二学期期末考试', '2016学年度第二学期总评', '2017学年度第一学期期中考试', '2017学年度第一学期平时成绩1', '2017-1学期考察科目总评', '2017学年度第一学期平时成绩2', '\t2017学年度第一学期期末考试', '2017学年度第一学期期末总评', '2017学年第二学期高一二平时成绩1', '2017学年度第二学期期中考试', '2017学年度第二学期平时成绩2', '2017学年度第二学期期末考试', '2017学年第二学期期末总评', '2018学年第一学期高三十校联考', '2018学年第一学期高三五校联考', '2018学年度第一学期平时成绩1', '2018-1学期期中考试', '2018学年度第一学期平时成绩2', '预测排名1', '预测排名2'];
    const rank = [31, 30, 35, 35, 37, 24, 37, 37, 21, 21, 18, 26, 34, 22, 13, 28, 17, 21, 22, 24, 21, 18, 17, 16];
    const rank_predict = [31, 30, 35, 35, 37, 24, 37, 37, 21, 21, 18, 26, 34, 22, 13, 28, 17, 21, 22, 24, 21, 18, 17, 16, 15, 20];
    const rank_down = [26, 26, 32, 32, 33, 19, 34, 34, 18, 19, 16, 24, 31, 20, 11, 23, 13, 16, 18, 19, 16, 15, 13, 12];
    const rank_up =  [8, 6, 5, 8, 6, 10, 6, 6, 9, 8, 7, 5, 4, 8, 6, 8, 10, 8, 5, 8, 9, 5, 6, 10];
    const option = {
        title: {
            text: '总分排名趋势',
            textStyle: {
                fontSize: 12 
            }
        },
        legend: {
            left: 'right',
            data: ['历史排名', '预测排名', '置信区间'],
        },
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                axis: 'x',
                type: 'line'
            },
            formatter: (params) => {
                if (params.length === 1) {
                    return params[0].name + '<br/>' + params[0].marker + params[0].data + '名';
                }
                return params[1].name + '<br/>' + params[1].marker + params[1].seriesName + ': ' + params[1].data + '<br/>' + params[2].marker + '置信区间: ' + params[2].data + '名~' + (params[2].data + params[3].data) + '名';
            }
        },
        grid:{
            left: 0,
            right: 0,
            top: '20%',
            bottom: '5%',
            containLabel: true
        },
        xAxis: {
            type: 'category',
            axisTick: {
                show: false
            },
            axisLabel: {
                show: false
            },
            data: xlabel
        },
        yAxis: {
            nameLocation: 'start',
            max: 50,
            min: 1,
            inverse: true,
            type: 'value',
            axisTick: {
                show: false
            },
            splitLine: {
                lineStyle: {
                    color: '#eeeeee',
                    type: 'dashed'
                }
            }
        },
        series: [{
            name: '预测排名',
            data: rank_predict,
            itemStyle: {
                color: '#df6b66'
            },
            type: 'line'
        },{
            name: '历史排名',
            data: rank,
            itemStyle: {
                color: '#90ca8f'
            },
            type: 'line'
        },{
            name: '置信区间',
            data: rank_down,
            type: 'line',
            itemStyle: {
                color: '#bdc0ba',
            },
            lineStyle: {
                    normal: {
                        opacity: 0
                    }
                },
                stack: 'confidence-band',
        },{
            name: '置信区间',
            data: rank_up,
            type: 'line',
            itemStyle: {
                color: '#bdc0ba',
            },
            lineStyle: {
                    normal: {
                        opacity: 0
                    }
                },
                areaStyle: {
                    normal: {
                        color: '#ccc'
                    }
                },
                stack: 'confidence-band',
        }]
    };
    return (
        <Ec option={option} h='150px' />
    )
}