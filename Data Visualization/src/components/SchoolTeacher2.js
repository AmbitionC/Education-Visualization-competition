import React from 'react';
import { Card } from 'react-bootstrap';
import Ec from './Ec';
import Intro from './Intro';

export default function() {
    const option = {
        color: ['#749aa0', '#df6b66', '#8cc1aa'],
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
            }
        },
        legend: {
            top: 'top',
            left: 'center',
            data: ['高一', '高二', '高三']
        },
        grid: {
            left: 0,
            right: 0,
            top: '16%',
            bottom: '2%',
            containLabel: true
        },
        xAxis: {
            type: 'category',
            axisTick: {
                show: false
            },
            data: ['语\n文', '数\n学', '英\n语', '物\n理', '化\n学', '政\n治', '历\n史', '生\n物', '地\n理', '技\n术', '美\n术', '体\n育', '音\n乐']
        },
        yAxis: {
            type: 'value',
            axisLabel: {
                formatter: '{value}人'
            },
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
        toolbox: {
            feature: {
                magicType: {show: true, type: ['stack']},
                restore: {show: true},
            }
        },
        series: [
            {
                name: '高一',
                type: 'bar',
                label: {
                    show: false,
                    position: 'top'
                },
                data: [24, 27, 47, 19, 18, 10, 9, 12, 11, 1, 3, 1, 2]
            },
            {
                name: '高二',
                type: 'bar',
                label: {
                    show: false,
                    position: 'top'
                },
                data: [22, 24, 40, 11, 8, 8, 4, 11, 4, 9, 3, 1, 2]
            },
            {
                name: '高三',
                type: 'bar',
                label: {
                    show: false,
                    position: 'top'
                },
                data: [21, 20, 32, 9, 10, 4, 4, 8, 4, 6, 2, 1, 2]
            },
        ]
    };
    const content = [
        '设计理念: 默认情况下，对某一学科的教师数量进行年纪对比；堆叠图时，可对比各学科教师总数',
        '功能: 帮助校领导层平衡学校教师的年级分配和学科分配'
    ];
    return (
        <Card>
            <Card.Header>
                <h4>1-2-2 师资分配</h4>
                <Intro content={content} />
            </Card.Header>
            <Card.Body>
                <Ec option={option} h='300px'/>
            </Card.Body>
        </Card>
    );
}