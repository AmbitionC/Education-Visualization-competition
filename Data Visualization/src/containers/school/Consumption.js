import React from 'react';
import Csp1 from '../../components/SchoolCsp1';
import Csp2 from '../../components/SchoolCsp2';
import Csp3 from '../../components/SchoolCsp3';
import Csp4 from '../../components/SchoolCsp4';
import Csp5 from '../../components/SchoolCsp5';

export default function() {
    return (
        <React.Fragment>
            <div className="row mb-3">
                <div className="col-lg">
                    <Csp1 />
                </div>
            </div>
            <div className="row mb-3">
                <div className="col-12 col-lg-9">
                    <Csp2 />
                </div>
                <div className="col-12 col-lg-3">
                    <Csp3 />
                </div>
            </div>
            <div className="row mb-3">
                <div className="col-12 col-lg-6">
                    <Csp4 />
                </div>
                <div className="col-12 col-lg-6">
                    <Csp5 />
                </div>
            </div>
        </React.Fragment>
    );
}
