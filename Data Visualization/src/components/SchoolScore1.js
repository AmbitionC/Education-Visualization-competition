import React, { Component } from 'react';
import { Card , DropdownButton, Dropdown } from 'react-bootstrap';
import Ec from './Ec';
import Intro from './Intro';
// import examClassScore from '../data/grade/school/exam_class_score.json';
import examClassTScore from '../data/grade/school/exam_class_t_score.json';

const SUB_TYPE = ['总分', '语文', '数学', '英语', '政治', '历史', '地理', '物理', '化学', '生物', '技术'];
const SCORE_TYPE = {
    // Score: examClassScore,
    T_Score: examClassTScore,
};
const EXAM_NAME = [
    '2018-1学期期中考试',
    '2018-1学期期末考试',
    '2018学年度第一学期平时成绩1',
    '2018学年度第一学期平时成绩2',
    '2018学年第一学期高三五校联考',
    '2018学年第一学期高三十校联考'
];
const colors = [
    '#749aa0',
    '#df6b66',
    '#e79d88',
    '#8cc1aa',
    '#ec7e55',
    '#72a375',
    '#efdd7d',
    '#71B9BC',
    '#7189aa',
    '#90CA8F',
    '#F59F48',
];

const getSeriesModel = (name, center, polarIndex, data) => {
    const rangeStack = name + '最大最小值' + polarIndex;
    const averageStack = name + '均值' + polarIndex;
    return [{
        name: name,
        center: center,
        polarIndex: polarIndex,
        stack: rangeStack,
        type: 'bar',
        itemStyle: {
            normal: {
                opacity: 0,
            }
        },
        data: data.map(d=>d[0]),
        coordinateSystem: 'polar',
        silent: true
    }, {
        name: name,
        center: center,
        polarIndex: polarIndex,
        stack: rangeStack,
        type: 'bar',
        data: data.map(d=>d[1]-d[0]),
        coordinateSystem: 'polar',
    }, {
        name: name,
        center: center,
        polarIndex: polarIndex,
        stack: averageStack,
        type: 'bar',
        itemStyle: {
            normal: {
                color: 'transparent'
            }
        },
        data: data.map(d=>d[2]),
        coordinateSystem: 'polar',
        silent: true,
        z: 10
    }, {
        name: name,
        center: center,
        polarIndex: polarIndex,
        stack: averageStack,
        type: 'bar',
        itemStyle: {
            color: '#4f4f48',
        },
        data: data.map(d=>d[2]/100),
        coordinateSystem: 'polar',
        barGap: '-100%',
        z: 10
    }];
};

const getGradeOption = (grade, examName, scoreType) => {
    const gradeIndex = {
        gradeOne: {
            center: ['16%', '55%'],
            polarIndex: 0,
        },
        gradeTwo: {
            center: ['50%', '55%'],
            polarIndex: 1,
        },
        gradeThree: {
            center: ['84%', '55%'],
            polarIndex: 2,
        },
    };
    const formatClassName = (oriName) => {
        return oriName.map((items)=>{
            if (items.indexOf('东') > -1 || items.indexOf('白') > -1) {
                return items[0] + items[5] + items[6] + '班';
            } else {
                return items[3] + items[4] + '班';
            }
        });
    };
    let series = [];
    for (let i in grade) {
        if (grade.hasOwnProperty(i)) {
            for(let j = 0; j < SUB_TYPE.length; j ++) {
                series = series.concat(getSeriesModel(SUB_TYPE[j], gradeIndex[i].center,gradeIndex[i].polarIndex, grade[i].data[j]));
            }
        }
    }
    return {
        color: colors,
        title: {
            left: 'center',
            text: examName,
            textStyle: {
                fontWeight: 400,
                fontSize: 16,
            }
        },
        legend: {
            show: true,
            data: SUB_TYPE,
            type: 'scroll',
            selectedMode: 'single',
            bottom: 'bottom',
        },
        tooltip: {
            show: true,
            formatter: params=>{
                let min, max, mean;
                const t = /\d{1,2}/.exec(params.seriesId)[0];
                if (t === '1' || t === '5' || t === '9') {
                    min = series[params.seriesIndex - 1].data[params.dataIndex];
                    max = series[params.seriesIndex].data[params.dataIndex] + min;
                    mean = series[params.seriesIndex + 1].data[params.dataIndex];
                } else if (t === '3' || t === '7' || t === '11') {
                    min = series[params.seriesIndex - 3].data[params.dataIndex];
                    max = series[params.seriesIndex - 2].data[params.dataIndex] + min;
                    mean = series[params.seriesIndex - 1].data[params.dataIndex];
                } else {
                    return '未知';
                }
                return params.name + '<br/>最高分: ' + max + '<br/>最低分: ' + min + '<br/>平均分: ' + mean;
            },
        },
        polar: [{
            center: gradeIndex.gradeOne.center,
            radius: '60%',
        }, {
            center: gradeIndex.gradeTwo.center,
            radius: '60%',
        }, {
            center: gradeIndex.gradeThree.center,
            radius: '60%',
        }],
        angleAxis: [{
            polarIndex: gradeIndex.gradeOne.polarIndex,
            type: 'category',
            data: formatClassName(grade.gradeOne.className),
            axisLabel: {
                interval: 0,
            },
            axisTick: {
                show: false,
            }
        }, {
            polarIndex: gradeIndex.gradeTwo.polarIndex,
            type: 'category',
            data: formatClassName(grade.gradeTwo.className),
            axisLabel: {
                interval: 0,
            },
            axisTick: {
                show: false,
            }
        }, {
            polarIndex: gradeIndex.gradeThree.polarIndex,
            type: 'category',
            data: formatClassName(grade.gradeThree.className),
            axisLabel: {
                interval: 0,
            },
            axisTick: {
                show: false,
            }
        }],
        radiusAxis: [{
            name: '高一',
            polarIndex: gradeIndex.gradeOne.polarIndex,
            splitNumber: 3,
            nameGap: 32,
            nameTextStyle: {
                fontSize: 14,
            },
            axisTick: {
                show: false,
            },
            axisLabel: {
                show: false,
            },
            axisLine: {
                show: false,
            },
            splitLine: {
                lineStyle: {
                    color: '#eeeeee',
                    type: 'dashed'
                }
            },
        }, {
            name: '高二',
            polarIndex: gradeIndex.gradeTwo.polarIndex,
            splitNumber: 3,
            nameGap: 32,
            nameTextStyle: {
                fontSize: 14,
            },
            axisTick: {
                show: false,
            },
            axisLabel: {
                show: false,
            },
            axisLine: {
                show: false,
            },
            splitLine: {
                lineStyle: {
                    color: '#eeeeee',
                    type: 'dashed'
                }
            },
        }, {
            name: '高三',
            polarIndex: gradeIndex.gradeThree.polarIndex,
            splitNumber: 3,
            nameGap: 32,
            nameTextStyle: {
                fontSize: 14,
            },
            axisTick: {
                show: false,
            },
            axisLabel: {
                show: false,
            },
            axisLine: {
                show: false,
            },
            splitLine: {
                lineStyle: {
                    color: '#eeeeee',
                    type: 'dashed'
                }
            },
        }],
        series: series,
    }
};

export default class extends Component {
    constructor(props) {
        super(props);
        this.state = {
            scoreType: undefined,
            examName: undefined,
        };
        this.grade = {
            gradeOne: {
                className: [],
                data: [],
            },
            gradeTwo: {
                className: [],
                data: [],
            },
            gradeThree: {
                className: [],
                data: [],
            },
        };
        this.option = null;
    }
    chooseScoreType(scoreType) {
        this.setGradeData(scoreType, this.state.examName);
    }
    chooseExam(idx) {
        this.setGradeData(this.state.scoreType, EXAM_NAME[idx]);
    }
    formatValue(x) {
        if (x === -1) {
            return undefined;
        }
        if (typeof x === 'string') {
            return parseFloat(x);
        }
        return x;
    }
    initDataArr() {
        for (let i in this.grade) {  // 遍历数据数组，如果不为空，则置空
            if (this.grade.hasOwnProperty(i)) {
                if (this.grade[i].className.length > 0) {
                    this.grade[i].className = [];
                }
                if (this.grade[i].data.length > 0) {
                    this.grade[i].data = [];
                }
            }
        }
        for (let i = 0; i < SUB_TYPE.length; i ++) {  // 初始化各科目数据存放空间
            this.grade.gradeOne.data.push([]);
            this.grade.gradeTwo.data.push([]);
            this.grade.gradeThree.data.push([]);
        }
    }
    setGradeData(scoreType, examName) {
        this.initDataArr();  // 初始化数据数组
        const pushData = (singleData, arr) => {  // 功能: 向数据数组中push数据
            for (let j = 0; j < SUB_TYPE.length; j ++) {
                const min = singleData[j * 3 + 3];
                const max = singleData[j * 3 + 2];
                const mean = singleData[j * 3 + 4];
                arr[j].push([this.formatValue(min), this.formatValue(max), this.formatValue(mean)]);
            }
        };
        // 遍历数据
        const data = SCORE_TYPE[scoreType].data;
        for (let i = 0; i < data.length; i ++) {
            const singleData = data[i];  // 某一行数据
            if (singleData[0] === examName) {  // 判断考试名
                if (singleData[1].indexOf('高一') > -1 && singleData[1].indexOf('IB') === -1) {  // 判断年级
                    this.grade.gradeOne.className.push(singleData[1]);  // 将高一年级的所有班级添加到className中
                    pushData(singleData, this.grade.gradeOne.data);  // 将高一年级的所有成绩添加到data中
                } else if (singleData[1].indexOf('高二') > -1) {
                    this.grade.gradeTwo.className.push(singleData[1]);
                    pushData(singleData, this.grade.gradeTwo.data);
                } else if (singleData[1].indexOf('高三') > -1) {
                    this.grade.gradeThree.className.push(singleData[1]);
                    pushData(singleData, this.grade.gradeThree.data);
                    if (singleData[0] === EXAM_NAME[4] || singleData[0] === EXAM_NAME[5]) {
                        pushData([], this.grade.gradeOne.data);
                        pushData([], this.grade.gradeTwo.data);
                    }
                } else {
                    console.log('*** 班级名称无法识别: ' + singleData[1] + ' ***');
                }
            }
        }
        this.option = getGradeOption(this.grade, examName, scoreType);
        this.setState({
            examName: examName,
            scoreType: scoreType,
        });
    }
    componentWillMount() {
        this.setGradeData('T_Score', EXAM_NAME[0]);
    }
    render() {
        return (
            <Card>
                <Card.Header>
                    <h4>1-3-3 班级成绩对比</h4>
                    <div className='flex-space-between align-items-center'>
                        <DropdownButton className='ml-2' bsPrefix='drop-down-btn' alignRight title="选择考试">
                            {EXAM_NAME.map((items, index) => {
                                return <Dropdown.Item
                                    key={index}
                                    bsPrefix='drop-down-items'
                                    onClick={this.chooseExam.bind(this, index)}>{items}</Dropdown.Item>;
                            })}
                        </DropdownButton>
                        {/* <DropdownButton className='ml-2' bsPrefix='drop-down-btn' alignRight title="分值类型">
                            {Object.keys(SCORE_TYPE).map((items, index) => {
                                return <Dropdown.Item
                                    key={index}
                                    bsPrefix='drop-down-items'
                                    onClick={this.chooseScoreType.bind(this, items)}>{items}</Dropdown.Item>;
                            })}
                        </DropdownButton> */}
                        <div>
                            <Intro content={[
                                '设计理念: 由于每次考试的难度不同，简单对比班级最高分、最低分、平均分的变化趋势意义不大，因此选取某一次考试来对比三个年级各班的最高分、最低分、平均分更能体现出班级的差别',
                                '功能: 帮助校领导层和科任教师了解各个班级的上限和下限，针对不同班级作出不同调整'
                                ]} />
                        </div>
                    </div>
                </Card.Header>
                <Card.Body>
                    <Ec option={this.option} h='360px' setOption={true}/>
                </Card.Body>
            </Card>
        );
    }
}