import React from 'react';
import { Card } from 'react-bootstrap';
import Ec from './Ec';
import jsonDateGender from '../data/consumption/school/date_gender.json';

export default function() {
    let money = [];
    let peoNum = [];
    let meanMoney = [];
    for (let i = 0; i < jsonDateGender.data.length; i ++) {
        const singleData = jsonDateGender.data[i];
        if (singleData[1] + singleData[2] >= 1000) {
            const date = singleData[0].replace(/\//g, '-');
            money.push([date, ((singleData[4] + singleData[5]) / 1000).toFixed(2)]);
            peoNum.push([date, singleData[1] + singleData[2]]);
            meanMoney.push([date, ((singleData[4] + singleData[5])/ (singleData[1] + singleData[2])).toFixed(2)]);
        }
    }
    const option = {
        color: ['#f59f48', '#8cc1aa', '#7189aa'],
        tooltip : {
            trigger: 'axis',
            axisPointer: {
                axis: 'x',
                type: 'line',
            },
            formatter: params => {
                let res = params.map((items, index) => {
                    const unitArr = ['千元', '人', '元']
                    return items.marker + items.seriesName + ': ' + items.data[1] + unitArr[index];
                });
                res.unshift(params[0].data[0]);
                return res.join('<br/>');
            }
        },
        legend: {
            top: 'top',
            left: 'center',
        },
        grid: {
            left: '2%',
            right: '1%',
            top: '12%',
            bottom: 0,
            containLabel: true
        },
        xAxis : [
            {
                type : 'time',
                boundaryGap : false,
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
            }
        ],
        yAxis : [
            {
                name: '金额/元或千元',
                type : 'value',
                axisTick: {
                    show: false
                },
                splitLine: {
                    show: false,
                    lineStyle: {
                        color: '#eeeeee',
                        type: 'dashed'
                    }
                }
            },
            {
                name: '人数/人',
                type: 'value',
                axisTick: {
                    show: false
                },
                splitLine: {
                    show: false,
                    lineStyle: {
                        color: '#eeeeee',
                        type: 'dashed'
                    }
                }
            },
        ],
        series : [
            {
                name: '消费总额',
                type: 'line',
                stack: '金额',
                symbol: 'none',
                smooth: true,
                data: money
            },
            {
                name: '消费人数',
                type: 'line',
                yAxisIndex: 1,
                symbol: 'none',
                smooth: true,
                data: peoNum
            },
            {
                name: '人均金额',
                type: 'line',
                symbol: 'none',
                smooth: true,
                data: meanMoney
            },
        ]
    };
    return (
        <Card>
            <Card.Header>
                <h4>1-5-2 消费趋势</h4>
            </Card.Header>
            <Card.Body>
                <Ec option={option} h='280px'/>
            </Card.Body>
        </Card>
    );
}