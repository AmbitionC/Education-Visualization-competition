import React, { Component } from 'react';
import { Card } from 'react-bootstrap';
import Ec from './Ec';
import Intro from './Intro';
import data from '../data/grade/school/sub_score.json';

export default class extends Component {
    constructor(props) {
        super(props);
        this.option = null;
    }
    retrieveScatterData(data, dimX, dimY) {
        var result = [];
        for (let i = 0; i < data.length; i++){
            let item = [data[i][dimX], data[i][dimY]];
            result.push(item);
        }
        return result;
    }
    generateGrid(option) {
        let index = 0;
        let sub_name = ['语文', '数学', '英语', '物理', '化学', '生物', '政治', '历史', '地理', '技术'];
        for (let i = 0; i < 2; i ++){
            for (let j = 0; j < 5; j ++){
                option.grid.push({
                    left: 4 + j * 19.5 + '%',
                    top: 8 + i * 50 + '%',
                    width: '16%',
                    height: '36%'
                });
                option.brush.xAxisIndex && option.brush.xAxisIndex.push(index);
                option.brush.yAxisIndex && option.brush.yAxisIndex.push(index);
                option.xAxis.push({
                    name: '班级',
                    nameLocation: 'center',
                    nameGap: 4,
                    gridIndex: index,
                    type: 'category',
                    data: data.xAxis,
                    axisLabel: {
                        show: false
                    },
                    axisTick: {
                        show: false
                    }
                });
                option.yAxis.push({
                    name: sub_name[i * 5 + j] + '等第成绩',
                    nameGap: 8,
                    gridIndex: index,
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
                });
                option.series.push({
                    type: 'scatter',
                    xAxisIndex: index,
                    yAxisIndex: index,
                    symbolSize: 5,
                    data: this.retrieveScatterData(data.score_total, 11, i*5+j),
                });
                index ++;
            }
        }
    }
    componentWillMount() {
        // const schema = [
        //     {name: 'Chinese', index: 1, text: '语文'},
        //     {name: 'Math', index: 2, text: '数学'},
        //     {name: 'English', index: 3, text: '英语'},
        //     {name: 'Physics', index: 4, text: '物理'},
        //     {name: 'Chemical', index: 5, text: '化学'},
        //     {name: 'Biology', index: 6, text: '生物'},
        //     {name: 'Policy', index: 7, text: '政治'},
        //     {name: 'History', index: 8, text: '历史'},
        //     {name: 'Geography', index: 9, text: '地理'},
        //     {name: 'Technology', index: 10, text: '技术'}
        // ];
        let option = {
            color: [ '#749aa0', '#df6b66', '#e79d88', '#8cc1aa', '#ec7e55', '#72a375', '#efdd7d', '#71B9BC', '#7189aa', '#90CA8F', '#F59F48'],
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
            // parallelAxis: [
            //     {dim: 0, name: schema[0].text},
            //     {dim: 1, name: schema[1].text},
            //     {dim: 2, name: schema[2].text},
            //     {dim: 3, name: schema[3].text},
            //     {dim: 4, name: schema[4].text},
            //     {dim: 5, name: schema[5].text},
            //     {dim: 6, name: schema[6].text},
            //     {dim: 7, name: schema[7].text},
            //     {dim: 8, name: schema[8].text},
            //     {dim: 9, name: schema[9].text},
            // ],
            // parallel: {
            //     bottom: '5%',
            //     top: '60%',
            //     left: '2%',
            //     right: '2%',
            //     parallelAxisDefault: {
            //         type: 'value',
            //         name: '成绩一览表',
            //         nameLocation: 'end',
            //         nameGap: 20,
            //         splitNumber: 3,
            //         nameTextStyle: {
            //             fontSize: 14
            //         },
            //         axisTick: {
            //             show: false,
            //         },
            //         splitLine: {
            //             show: false
            //         },
            //         axisLabel: {
            //             textStyle: {
            //                 color: '#555'
            //             }
            //         }
            //     }
            // },
            series: [
                // {
                //     name: 'parallel',
                //     type: 'parallel',
                //     smooth: true,
                //     lineStyle: {
                //         normal: {
                //             width: 1,
                //             opacity: 0.3
                //         }
                //     },
                //     data: data.score_total
                // }
            ],
        };
        this.generateGrid(option);
        this.option = option;
    }
    render() {
        return (
            <Card>
                <Card.Header>
                    <h4>1-3-6 班级成绩分布对比</h4>
                    <Intro content={[
                        '设计理念: 通过散点图与平行坐标系展示各个班级的成绩分布，组件可通过右上角圈选工具来选择数据并查看',
                        '功能: 用于观察学科之间的内在联系，以及各班级学生的考试成绩分布，帮助科任教师针对学科成绩较差的班级作出调整'
                        ]}/>
                </Card.Header>
                <Card.Body>
                    <Ec option={this.option} h='400px'/>
                </Card.Body>
            </Card>
        );
    }
}