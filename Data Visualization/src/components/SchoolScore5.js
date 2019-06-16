import React from 'react';
import { Card } from 'react-bootstrap';
import Ec from './Ec';
import Intro from './Intro';

export default function() {
    const option = {
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'line'
            },
            formatter: params => params[0].name + '<br/>第1名 ' + params[0].value + '分<br/>第30名 ' + params[1].value + '分'
        },
        grid: {
            left: 0,
            right: '3%',
            top: '5%',
            bottom: '5%',
            containLabel: true
        },
        xAxis: {
            type: 'category',
            boundaryGap: false,
            axisTick: {
                show: false,
            },
            splitLine: {
                show: false,
            },
            data: ['2013年', '2014年', '2015年', '2016年', '2017年', '2018年']
        },
        yAxis: {
            type: 'value',
            min: 500,
            max: 700,
            axisTick: {
                show: false,
            },
            splitLine: {
                show: false,
            },
            axisLabel: {
                formatter: '{value}分'
            }
        },
        series: [{
            data: [667, 632, 647, 625, 643.3, 635],
            type: 'line',
            symbol: 'none',
            smooth: true,
            itemStyle: {
                color: '#df6b66',
            },
            areaStyle: {
                opacity: 1,
            }
        }, {
            data: [607.5, 590, 596, 583.3, 605, 590],
            type: 'line',
            smooth: true,
            symbol: 'none',
            itemStyle: {
                color: '#df6b66',
            },
            areaStyle: {
                color: '#fff',
                opacity: 1
            }
        }]
    };
    const content = [
        '设计理念: 选取每年高三五校联考的第1名和第30名的成绩，观察他们的趋势',
        '功能: 帮助校领导层了解学校教育质量变化趋势'
    ];
    return (
        <Card>
            <Card.Header>
                <h4>1-3-1 顶尖毕业生历年成绩趋势</h4>
                <Intro content={content} />
            </Card.Header>
            <Card.Body>
                <Ec option={option} h='240px'/>
            </Card.Body>
        </Card>
    );
}