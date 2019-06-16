import React from 'react';
import { Card } from 'react-bootstrap';
import Ec from './Ec';
import Intro from './Intro';
import jsonData from '../data/consumption/school/poor_stu_csp_money.json';

const getSeries = () => {
    const stuIndex = [0, 51, 128, 299, 306, 457, 552, 675, 821, 988, 1164, 1296, 1462, 1621, 1777, 1922, 2088, 2260, 2429, 2543, 2712, 2719, 2746, 2863, 3022, 3173, 3265, 3333, 3428, 3540, 3661, 3683, 3710, 3862, 3884, 3925, 4087, 4157, 4277, 4414, 4536, 4698, 4864, 5033, 5047, 5168, 5283, 5427, 5544, 5634, 5709, 5806, 5936, 5998, 6125, 6186, 6233]
    const colors = ['#72a375', '#71b9bc', '#efdd7d', '#e79d88', '#df6b66'];
    let series = [];
    let date = new Set();
    for (let i = 0; i < stuIndex.length - 1; i ++) {
        let arr = [];
        let pre = '';
        let cnt = 0;
        for (let j = stuIndex[i]; j < stuIndex[i+1]; j ++) {
            const singleData = jsonData.data[j];
            date.add(singleData[0]);
            if (singleData[0] !== pre) {
                cnt = 0;
                if (arr[0]) {
                    arr[0].push([singleData[0], singleData[1]]);
                } else {
                    arr[0] = [];
                    arr[0].push([singleData[0], singleData[1]]);
                }
                pre = singleData[0];
            } else {
                if (arr[cnt]) {
                    arr[cnt].push([singleData[0], singleData[1]]);
                } else {
                    arr[cnt] = [];
                    arr[cnt].push([singleData[0], singleData[1]]);
                }
            }
            cnt += 1
        }
        // 此时arr中存放的是某个学生的数据
        for (let k = 0; k < arr.length; k ++) {
            series.push({
                type: 'bar',
                name: jsonData.index[stuIndex[i]],
                stack: jsonData.index[stuIndex[i]],
                itemStyle: {
                    color: colors[k],
                },
                data: arr[k],
            });
        }
    }
    return [Array.from(date).sort(), series];
}

export default function() {
    const [xData, series] = getSeries();
    const option = {
        grid: {
            left: 0,
            right: '2%',
            top: '12%',
            bottom: 0,
            containLabel: true
        },
        legend: {
            type: 'scroll',
            selectedMode: 'single',
        },
        tooltip: {
            formatter: params => [
                params.name,
                params.seriesName,
                '第' + (params.seriesIndex + 1) + '次消费: ' + params.data[1] + '元'
            ].join('<br/>')
        },
        xAxis: {
            type: 'category',
            data: xData,
            axisTick: {
                show: false
            },
            splitLine: {
                show: false
            },
            axisLabel: {
                formatter: (value, index) => {
                    const date = new Date(value);
                    const texts = [(date.getMonth() + 1), date.getDate()];
                    return texts.join('/');
                }
            },
        },
        yAxis: {
            type: 'value',
            axisLabel: {
                formatter: '{value}元'
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
        series: series
    };
    const content = [
        '设计理念: 采用柱状图展示贫困生的每次消费的情况，通过图例可以查看不同贫困生',
        '功能: 帮助校领导层了解每个贫困生的消费情况，针对异常情况及时干预',
    ];
    return (
        <Card>
            <Card.Header>
                <h4>1-5-5 贫困生消费总览</h4>
                <Intro content={content} />
            </Card.Header>
            <Card.Body>
                <Ec option={option} h='360px'/>
            </Card.Body>
        </Card>
    );
}