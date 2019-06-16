import React from 'react';
import Ec from './Ec'

const xlabel = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'];
const dataset = {'student': [4, 1, 4, 0, 0, 5, 0, 0, 6, 5, 0, 2], 'class': [4, 7, 1, 8, 1, 9, 0, 0, 0, 5, 2, 1], 'school': [2, 7, 0, 7, 10, 10, 0, 0, 9, 0, 4, 4]}
export default function(){
    const option = {
        title: {
            text: '校服校徽次数',
            textStyle: {
                fontSize: 12 
            }
        },
        legend: {
            data: ['学生', '班级平均', '学校平均']
        },
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                axis: 'x',
                type: 'shadow',
            }
        },
        grid: {
            left: 0,
            right: 0,
            top: '15%',
            bottom: '8%',
            containLabel: true
        },
        xAxis: {
            name: '月份',
            type: 'category',
            data: xlabel,
            axisTick: {
                show: false
            },
        },
        yAxis: {
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
            name: '学生',
            itemStyle: {
                color: '#df6b66'
            },
            data: dataset.student,
            type: 'line'
        },{
            name: '班级平均',
            itemStyle: {
                color: '#90ca8f'
            },
            data: dataset.class,
            type: 'line'
        },{
             name: '学校平均',
            itemStyle: {
                color: '#7189aa'
            },
            data: dataset.school,
            type: 'line'
        }]
    };
    return (
        <Ec option={option} h='200px'/>
    )
}    