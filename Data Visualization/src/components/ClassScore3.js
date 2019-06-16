import React from 'react';
import { Card } from 'react-bootstrap';
import Ec from './Ec';
import Intro from './Intro';
import jsonBoxData from '../data/grade/class/class920_box_data.json';
import jsonBoxOutlier from '../data/grade/class/class920_box_outlier.json';

export default class extends React.Component {
    constructor(props) {
        super(props);
        this.option = null;
    }
    componentWillMount() {
        let boxObj = {};
        const subArr = ['语文','数学','英语','物理','化学','生物','政治','历史','地理','技术'];
        for (let i = 0; i < jsonBoxData.index.length; i ++) {
            if (!boxObj[jsonBoxData.index[i]]) {
                boxObj[jsonBoxData.index[i]] = [ [], [], [], [], [], [], [], [], [], [] ];
            }
            const subIdx = subArr.indexOf(jsonBoxData.data[i][5]);
            if (subIdx > -1 ) {
                boxObj[jsonBoxData.index[i]][subIdx] = jsonBoxData.data[i];
            }
        }
        let outObj = {};
        for (let i = 0; i < jsonBoxOutlier.index.length; i ++) {
            if (!outObj[jsonBoxOutlier.index[i]]) {
                outObj[jsonBoxOutlier.index[i]] = [];
            }
            if (jsonBoxOutlier.data[i][1] !== '总分') {
                outObj[jsonBoxOutlier.index[i]].push([jsonBoxOutlier.data[i][1], jsonBoxOutlier.data[i][0]])
            }
        }
        let series = [];
        for (let examName in boxObj) {
            series.push({
                name: examName,
                type: 'boxplot',
                data: boxObj[examName],
                itemStyle: {
                    borderColor: '#7189aa'
                },
                tooltip: {
                    formatter: function (param) {
                        return [
                            param.name,
                            '上边界: ' + param.data[5],
                            '上四分位数: ' + param.data[4],
                            '中位数: ' + param.data[3],
                            '下四分位数: ' + param.data[2],
                            '下边界: ' + param.data[1]
                        ].join('<br/>');
                    }
                }
            });
            if (outObj[examName]) {
                series.push({
                    name: examName,
                    type: 'scatter',
                    itemStyle: {
                        color: '#e79d88'
                    },
                    data: outObj[examName]
                });
            }
        }
        this.option = {
            color: ['#df6b66', '#90ca8f', '#e79d88', '#8cc1aa', '#749aa0', '#72a375', '#efdd7d', '#ec75ee', '#7189aa', '#71b9bc', '#F59F48'],
            legend: {
                type: 'scroll',
                selectedMode: 'single',
                bottom: 'bottom'
            },
            tooltip: {},
            grid: {
                left: 0,
                right: 0,
                top: '10%',
                bottom: '10%',
                containLabel: true
            },
            xAxis: {
                type: 'category',
                data: subArr,
                boundaryGap: true,
                nameGap: 30,
                splitLine: {
                    show: false
                },
                axisTick: {
                    show: false
                },
            },
            yAxis: {
                type: 'value',
                name: '分数',
                splitLine: {
                    show: true,
                    lineStyle: {
                        color: '#eee',
                        type: 'dashed'
                    }
                },
                axisLine: {
                    show: false
                },
                axisTick: {
                    show: false
                }
            },
            series: series
        };
    }
    render() {
        return (
            <Card>
                <Card.Header>
                    <h4>2-2 成绩箱形图</h4>
                    <Intro content={[
                        '设计理念: 箱形图可以直观的展示班级学生的成绩分布情况',
                        '功能: 帮助科任教师了解班级内是否有特别优秀的学生以及成绩较差的学生，然后作出针对性调整'
                    ]} />
                </Card.Header>
                <Card.Body>
                    <Ec option={this.option} h='320px'/>
                </Card.Body>
            </Card>
        );
    }
}
