import React, { Component } from 'react';
import { Card , Button , Modal , Row , Col , Container , InputGroup , FormControl } from 'react-bootstrap';
import Ec from './Ec'
import jsonData from '../data/app/grade2_sub_trend.json';

class Example extends React.Component {
    constructor(props, context) {
        super(props, context);
    
        this.handleShow = this.handleShow.bind(this);
        this.handleClose = this.handleClose.bind(this);
    
        this.state = {
            show: false,
        };

        this.stuArr = [14460, 14471, 14505, 14465, 14506, 14494, 14462, 14473, 14458, 14498, 14507, 14466, 14472, 14463, 14499, 14474, 14491, 14487, 14459, 14464, 14496, 14475, 14479, 14511, 14461, 14493, 14478, 14492, 14508, 14476, 14455, 14504, 14500, 14512, 14469, 14501, 14486, 14481, 14454, 14502, 14470, 14483, 14488, 14489, 14482, 14503, 14513, 14497, 14495, 14477, 14456, 14480, 14457, 14468, 14467, 14510, 14620, 14900, 14930, 14798, 14910, 14892, 14886, 14940, 14923, 14937, 14905, 14916, 14864, 14889, 14929, 14897, 14894, 14538, 14661, 14902, 14906, 14817, 14549, 14769, 14525, 14687, 14571, 14861, 14728, 14751, 14771, 14529, 14556, 14618, 14553, 14725, 14873, 14848, 14563, 14734, 14598, 14932, 14693, 14887, 14935, 14903, 14757, 14885, 14917, 14871, 14775, 14904, 14583, 14707, 14692, 14852, 14920, 14888, 14565, 14518, 14710, 14677, 14662, 14740, 14548, 14516, 14534, 14933, 14901, 14694, 14806, 14934, 14790, 14854, 14918, 14611, 14884, 14870, 14926, 14600, 14664, 14912, 14891, 14859, 14667, 14635, 14785, 14539, 14913, 14784, 14860, 14632, 14668, 14863, 14895, 14572, 14606, 14670, 14893, 14797, 14753, 14914, 14882, 14818, 14835, 14595, 14627, 14755, 14921, 14883, 14761, 14915, 14665, 14562, 14633, 14594, 14722, 14922, 14858, 14602, 14754, 14669, 14936, 14879, 14584, 14896, 14909, 14686, 14586, 14715, 14866, 14585, 14898, 14779, 14609, 14617, 14814, 14527, 14846, 14810, 14672, 14907, 14705, 14939, 14621, 14833, 14522, 14942, 14713, 14941, 14928, 14745, 14587, 14908, 14876, 14684, 14943, 14526, 14872, 14931, 14622, 14555, 14623, 14619, 14706, 14938, 14911, 14899, 14844, 14746, 14787, 14826, 14878, 14794, 14654, 14714, 14666, 14782, 14634, 14750, 14682, 14558, 14590, 14699, 14819, 14691, 14827, 14603, 14749, 14796, 14881, 14927, 14799, 14735, 14639, 14849, 14575, 14543, 14780, 14524, 14523, 14944, 14812, 14880, 14560, 14688, 14656, 14588, 14593, 14764, 14875, 14732, 14700, 14604, 14557, 14658, 14717, 14690, 14803, 14638, 14850, 14541, 14813, 14683, 14877, 14651, 14702, 14829, 14815, 14842, 14758, 14776, 14741, 14680, 14648, 14645, 14726, 14581, 14545, 14840, 14774, 14592, 14614, 14582, 14550, 14737, 14777, 14869, 14738, 14544, 14663, 14739, 14514, 14579, 14547, 14631, 14578, 14610, 14695, 14855, 14727, 14759, 14772, 14708, 14676, 14644, 14823, 14865, 14552, 14839, 14793, 14704, 14628, 14536, 14559, 14724, 14825, 14655, 14551, 14697, 14719, 14788, 14601, 14874, 14537, 14681, 14624, 14629, 14597, 14679, 14711, 14576, 14640, 14531, 14528, 14567, 14851, 14811, 14809, 14756, 14650, 14841, 14535, 14843, 14791, 14554, 14786, 14747, 14659, 14822, 14521, 14616, 14649, 14789, 14821, 14853, 14630, 14744, 14625, 14723, 14530, 14532, 14808, 14919, 14689, 14596, 14721, 14657, 14867, 14783, 14800, 14519, 14736, 14768, 14856, 14824, 14792, 14760, 14696, 14743, 14568, 14591, 14857, 14847, 14890, 14762, 14731, 14608, 14807, 14924, 14805, 14675, 14515, 14868, 14612, 14580, 14770, 14837, 14709, 14801, 14613, 14517, 14641, 14742, 14673, 14678, 14646, 14718, 14647, 14828, 14607, 14830, 14862, 14542, 14573, 14652, 14605, 14701, 14765, 14685, 14767, 14574, 14703, 14671, 14589, 14636, 14816, 14540, 14733, 14763, 14838, 14795, 14781, 14570, 14643, 14637, 14766, 14674, 14836, 14834, 14773, 14804, 14569, 14660, 14599, 14831, 14712, 14748, 14845, 14698, 14626, 14820, 14752, 14730, 14778, 14615, 14533];
    }
  
    handleClose() {
        this.setState({ show: false });
    }
  
    handleShow() {
        this.setState({ show: true });
    }

    getStudentList() {
        let mat = [];
        for (let i = 0; i < this.stuArr.length; i ++) {
            const row = parseInt(i/6);
            if (!mat[row]) {
                mat.push([this.stuArr[i]]);
            } else {
                mat[row].push(this.stuArr[i]);
            }
        }
        return mat;
    }
 
    shouldComponentUpdate(nextProps, nextState) {
        if (nextState.show !== this.state.show) {
            return true;
        }
        return false;
    }

    render() {
        this.getStudentList();
        return (
            <>
                <button className="badge badge-success border-0 ml-2" onClick={this.handleShow}>
                    选择学生
                </button>
                <Modal show={this.state.show} onHide={this.handleClose} size="lg">
                    <Modal.Header closeButton>
                    <Modal.Title>目前支持的学生列表</Modal.Title>
                    </Modal.Header>
                    <Modal.Body>
                        <Container style={{height: '240px'}} className='overflow-y-scroll'>
                            {
                                this.getStudentList().map((items, index) => {
                                    return (
                                        <Row className='show-grid' key={index}>
                                            {
                                                items.map((items, index) => {
                                                    return (
                                                        <Col key={index} md={2}>
                                                            <span>{items}</span>
                                                        </Col>
                                                    );
                                                })
                                            }
                                        </Row>
                                    );
                                })
                            }
                        </Container>
                    </Modal.Body>
                    <Modal.Footer>
                        <InputGroup size='sm' style={{width: '36%'}}>
                            <FormControl
                            placeholder="请输入学生ID"
                            aria-describedby="basic-addon2"
                            ref={input=>{
                                if (input && input.value) {
                                    const idx = this.stuArr.indexOf(Number(input.value));
                                    if (idx === -1) {
                                        alert('该学生不在列表中');
                                    } else {
                                        this.props.changeStu(this.stuArr[idx]);
                                    }
                                }
                            }}
                            />
                            <InputGroup.Append>
                                <Button variant='outline-primary' onClick={this.handleClose}>确定</Button>
                            </InputGroup.Append>
                        </InputGroup>
                    </Modal.Footer>
                </Modal>
            </>
        );
    }
}


export default class extends Component {
    constructor(props) {
        super(props);
        this.state = {
            id: 0
        };
        this.option = {};
        this.option2 = {};
        this.option3 = {};

        this.setOption = this.setOption.bind(this);
    }
    calMAX(arr) {
        if (arr.length === 0) {
            return;
        }
        return Math.max.apply(null, arr.filter(item=>item));
    }
    calMIN(arr) {
        if (arr.length === 0) {
            return;
        }
        return Math.min.apply(null, arr.filter(item=>item));
    }
    calMEAN(arr) {
        const N = arr.length;
        let sum = 0;
        for (let i = 0; i < N; i ++) {
            sum += arr[i];
        }
        return sum/N;
    }
    calSTD(arr) {
        const N = arr.length;
        if (N === 0) {
            return;
        }
        const MEAN = this.calMEAN(arr);
        let sumOfSquare = 0;
        for (let i = 0; i < N; i ++) {
            sumOfSquare += (arr[i] - MEAN) * (arr[i] - MEAN)
        }
        return Math.sqrt(sumOfSquare/N);
    }
    STDtoStability(arr) {
        const MIN = 60;
        const MAX = 100;
        const length = arr.length;
        const max = this.calMAX(arr);
        const min = this.calMIN(arr);
        const step = (MAX - MIN) / (max - min);
        let res = [];
        for (let i = 0; i < length; i ++) {
            res.push((max - arr[i]) * step + MIN);
        }
        return res;
    }
    calRecommScore(meanArr, stdArr, maxArr, minArr) {
        const len = meanArr.length;
        if (!meanArr[len-1]) {
            meanArr = meanArr.slice(0, len-1);
        }
        if (!stdArr[len-1]) {
            stdArr = stdArr.slice(0, len-1);
        }
        if (!maxArr[len-1]) {
            maxArr = maxArr.slice(0, len-1);
        }
        if (!minArr[len-1]) {
            minArr = minArr.slice(0, len-1);
        }
        const MEAN_WEIGHT = 0.4;
        const STD_WEIGHT = 0.3;
        const MAX_WEIGHT = 0.2;
        const MIN_WEIGHT = 0.1;
        const meanMAX = Math.max.apply(null, meanArr);
        const meanMIN = Math.min.apply(null, meanArr);
        const stdMAX = Math.max.apply(null, stdArr);
        const stdMIN = Math.min.apply(null, stdArr);
        const maxMAX = Math.max.apply(null, maxArr);
        const maxMIN = Math.min.apply(null, maxArr);
        const minMAX = Math.max.apply(null, minArr);
        const minMIN = Math.min.apply(null, minArr);
        let res = [];
        for (let i = 0; i < len; i ++) {
            res.push(
                MEAN_WEIGHT * (meanArr[i] - meanMIN) / (meanMAX - meanMIN) +
                STD_WEIGHT * (stdArr[i] - stdMIN) / (stdMAX - stdMIN) +
                MAX_WEIGHT * (maxArr[i] - maxMIN) / (maxMAX - maxMIN) +
                MIN_WEIGHT * (minArr[i] - minMIN) / (minMAX - minMIN)
            );
        }
        return res;
    }
    setOption(id) {
        const data = jsonData[id];
        const subMap = {
            'wl': '物理',
            'hx': '化学',
            'sw': '生物',
            'zz': '政治',
            'ls': '历史',
            'dl': '地理',
            'js': '技术'
        }
        let series = [];
        let std = [];
        let max = [];
        let min = [];
        let mean = [];
        for (let sub in data) {
            const subData = data[sub].map(items => items>0?items:undefined)
            const calData = subData.filter(item=>item)
            series.push({
                name: subMap[sub],
                type: 'line',
                smooth: true,
                connectNulls: true,
                data: subData
            });
            std.push(this.calSTD(calData));
            max.push(this.calMAX(calData));
            min.push(this.calMIN(calData));
            mean.push(this.calMEAN(calData));
        }
        this.option = {
            color: ['#749aa0', '#df6b66', '#e79d88', '#8cc1aa', '#ec7e55', '#72a375', '#efdd7d', '#71B9BC', '#7189aa', '#90CA8F', '#F59F48'],
            tooltip: {},
            legend: {
                left: 'center',
                bottom: 'bottom',
                type: 'scroll'
            },
            title: {
                text: '成绩趋势',
                left: 'center',
                textStyle: {
                    fontWeight: 500,
                    fontSize: 15,
                }
            },
            grid: {
                left: 0,
                right: '5%',
                top: '12%',
                bottom: '15%',
                containLabel: true
            },
            xAxis: {
                name: '考试',
                nameLocation: 'center',
                nameGap: 10,
                type: 'category',
                axisTick: {
                    show: false
                },
                axisLabel: {
                    show: false
                },
                data: ['2017-1期中考试', '2017-1期末考试', '2017-1期末总评', '2017-2期中考试', '2017-2期末考试', '2017-2期末总评', '2018-1期中考试']
            },
            yAxis: {
                type: 'value',
                min: 40,
                axisTick: {
                    show: false
                },
                splitLine: {
                    lineStyle: {
                        color: '#eeeeee',
                        type: 'dashed'
                    }
                },
            },
            series: series 
        };
        this.option2 = {
            color: ['#749aa0', '#df6b66', '#e79d88', '#8cc1aa', '#ec7e55', '#72a375', '#efdd7d', '#71B9BC', '#7189aa', '#90CA8F', '#F59F48'],
            tooltip: {
                formatter: params => params.name + '<br/>' + params.marker + params.data.toFixed(2)
            },
            grid: [
                {containLabel: false, left: '8%', right: '57%', top: '8%', bottom: '62%'},
                {containLabel: false, left: '8%', right: '57%', top: '60%', bottom: '10%'},
                {containLabel: false, left: '63%', right: '2%', top: '8%', bottom: '62%'},
                {containLabel: false, left: '63%', right: '2%', top: '60%', bottom: '10%'}
            ],
            xAxis: [{
                type: 'category',
                data: ['物理', '化学', '生物', '政治', '历史', '地理', '技术'],
                axisTick: {
                    show: false
                },
                axisLabel: {
                    formatter: param => param[0] + '\n' + param[1]
                }
            }, {
                gridIndex: 1,
                type: 'category',
                data: ['物理', '化学', '生物', '政治', '历史', '地理', '技术'],
                axisTick: {
                    show: false
                },
                axisLabel: {
                    formatter: param => param[0] + '\n' + param[1]
                }
            }, {
                gridIndex: 2,
                type: 'category',
                data: ['物理', '化学', '生物', '政治', '历史', '地理', '技术'],
                axisTick: {
                    show: false
                },
                axisLabel: {
                    formatter: param => param[0] + '\n' + param[1]
                }
            }, {
                gridIndex: 3,
                type: 'category',
                data: ['物理', '化学', '生物', '政治', '历史', '地理', '技术'],
                axisTick: {
                    show: false
                },
                axisLabel: {
                    formatter: param => param[0] + '\n' + param[1]
                }
            }],
            yAxis: [{
                type: 'value',
                name: '平均分',
                axisTick: {
                    show: false
                },
                splitLine: {
                    lineStyle: {
                        color: '#eeeeee',
                        type: 'dashed'
                    }
                },
            }, {
                gridIndex: 1,
                type: 'value',
                name: '稳定性',
                axisTick: {
                    show: false
                },
                splitLine: {
                    lineStyle: {
                        color: '#eeeeee',
                        type: 'dashed'
                    }
                },
            }, {
                gridIndex: 2,
                type: 'value',
                name: '最高分',
                axisTick: {
                    show: false
                },
                splitLine: {
                    lineStyle: {
                        color: '#eeeeee',
                        type: 'dashed'
                    }
                },
            }, {
                gridIndex: 3,
                type: 'value',
                name: '最低分',
                axisTick: {
                    show: false
                },
                splitLine: {
                    lineStyle: {
                        color: '#eeeeee',
                        type: 'dashed'
                    }
                },
            }],
            series: [{
                type: 'bar',
                data: mean,
            }, {
                type: 'bar',
                xAxisIndex: 1,
                yAxisIndex: 1,
                data: this.STDtoStability(std),
            }, {
                type: 'bar',
                xAxisIndex: 2,
                yAxisIndex: 2,
                data: max,

            }, {
                type: 'bar',
                xAxisIndex: 3,
                yAxisIndex: 3,
                data: min,
            }]
        };
        const recomm = this.calRecommScore(mean, this.STDtoStability(std), max, min);
        const t = recomm.slice(0);
        const [fir, sec, thi, fou] = t.sort((a, b) => b-a);
        let recommData = [];
        const subNameArr = ['物理', '化学', '生物', '政治', '历史', '地理', '技术'];
        const recommColor = ['#df6b66', '#7189aa', '#5dac81'];
        for (let i = 0; i < recomm.length; i ++) {
            if (recomm[i] > sec) {
                recommData.push({
                    name: subNameArr[i],
                    value: recomm[i],
                    itemStyle: {
                        color: recommColor[0]
                    }
                });
            } else if (recomm[i] > thi) {
                recommData.push({
                    name: subNameArr[i],
                    value: recomm[i],
                    itemStyle: {
                        color: recommColor[1]
                    }
                });
            } else if (recomm[i] > fou) {
                recommData.push({
                    name: subNameArr[i],
                    value: recomm[i],
                    itemStyle: {
                        color: recommColor[2]
                    }
                });
            } else {
                recommData.push({
                    name: subNameArr[i],
                    value: recomm[i],
                    itemStyle: {
                        color: '#c0c0c0'
                    }
                })
            }
        }
        this.option3 = {
            title : {
                text: '学生' + id + '的七选三推荐方案',
                x:'center',
                textStyle: {
                    fontWeight: 500,
                    fontSize: 15,
                }
            },
            series : [
                {
                    type:'pie',
                    radius : [20, 90],
                    roseType : 'radius',
                    hoverAnimation: false,
                    label: {
                        show: true,
                        formatter: param => param.name + '\n推荐指数\n' + param.value.toFixed(6)
                    },
                    labelLine: {
                        length: 5,
                        length2: 5
                    },
                    data: recommData
                },
            ]
        };
        this.setState({
            id: id
        });
    }
    componentWillMount() {
        this.setOption(14460);
    }
    render() {
        return (
            <Card>
                <Card.Header>
                    <h4>4-3-1 学科七选三推荐</h4>
                    <Example changeStu={this.setOption}/>
                </Card.Header>
                <Card.Body>
                    <div className='row'>
                        <div className='col-12 col-lg-3'>
                            <Ec option={this.option} h='360px' resetOption={true}/>
                        </div>
                        <div className='col-12 col-lg-1 align-items-center justify-content-center'>
                            <div className='right-arrow'></div>
                        </div>
                        <div className='col-12 col-lg-4'>
                            <Ec option={this.option2} h='360px' resetOption={true}/>
                        </div>
                        <div className='col-12 col-lg-1 align-items-center justify-content-center'>
                            <div className='right-arrow'></div>
                        </div>
                        <div className='col-12 col-lg-3'>
                            <Ec option={this.option3} h='360px' resetOption={true}/>
                        </div>
                    </div>
                </Card.Body>
            </Card>
        )
    }
}
