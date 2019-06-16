import React from 'react';
import Info1 from '../../components/SchoolInfo1';
import Info2 from '../../components/SchoolInfo2';
import Info3 from '../../components/SchoolInfo3';
import Info4 from '../../components/SchoolInfo4';

export default function() {
    return (
        <React.Fragment>
            <div className='row mb-3'>
                <div className='col-12 col-lg-7'>
                    <Info1 />
                </div>
                <div className='col-12 col-lg-5'>
                    <Info2 />
                </div>
            </div>
            <div className='row mb-3'>
                <div className='col-12 col-lg-9'>
                    <Info3 />
                </div>
                <div className='col-12 col-lg-3'>
                    <Info4 />
                </div>
            </div>
        </React.Fragment>
    );
}
