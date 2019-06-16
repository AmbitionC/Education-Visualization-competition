import React from 'react';
import Ec from './Ec'

const xlabel = ['2017学年度第一学期期末总评', '2017学年第二学期高一二平时成绩1', '2018学年度第一学期平时成绩1', '2017学年度第二学期平时成绩2', '2017学年度第二学期期中考试', '\t2017学年度第一学期期末考试', '\t2017学年度第一学期期末考试', '2017学年度第一学期平时成绩2', '预测排名1', '预测排名2'];
const rank_technology = [4, 21, 4, 13, 26, 42, 4, 13];
const rank_music = [17, 19, 24, 22, 20, 15, 12, 21];
const rank_sport = [14, 38, 32, 28, 25, 32, 37, 29];
const rank_technology_predict = [4, 21, 4, 13, 26, 42, 4, 13, 10, 15];
const rank_music_predict = [17, 19, 24, 22, 20, 15, 12, 21, 19, 25];
const rank_sport_predict = [14, 38, 32, 28, 25, 32, 37, 29, 26, 30];

export default function (){
    const option = {
        title: {
            text: '考查课排名趋势',
            textStyle: {
                fontSize: 12 
            }
        },
        legend: {
            left: 'right',
            data: ['美术', '体育', '音乐'],
        },
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                axis: 'x',
                type: 'line'
            }
        },
        grid: {
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
            name: '美术',
            data: rank_technology_predict,
            itemStyle: {
                color: '#e79d88' 
            },
            lineStyle: {
                type: 'dashed'
            },
            type: 'line'
        },{
            name: '体育',
            data: rank_sport_predict,
            itemStyle: {
                color: '#8cc1aa'
            },
            lineStyle: {
                type: 'dashed'
            },
            type: 'line'
        },{
            name: '音乐',
            data: rank_music_predict,
            itemStyle: {
                color: '#71b9bc'
            },
            lineStyle: {
                type: 'dashed'
            },
            type: 'line'
        },{
            name: '美术',
            data: rank_technology,
            itemStyle: {
                color: '#e79d88' 
            },
            type: 'line'
        },{
            name: '体育',
            data: rank_sport,
            itemStyle: {
                color: '#8cc1aa'
            },
            type: 'line'
        },{
            name: '音乐',
            data: rank_music,
            itemStyle: {
                color: '#71b9bc'
            },
            type: 'line'
        }] 
    };
    return (
        <Ec option={option} h='153px'/>
    )
}
