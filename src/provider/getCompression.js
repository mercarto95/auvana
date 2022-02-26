import { pyProcess } from "../controller/pyProcess";
import { apiArgs, epMode } from '../utils/config';


function getCompression(callback) {
    pyProcess(epMode.POST,
        (datas) => {
            callback(JSON.parse(datas.toString("utf8")));
        },
        [apiArgs.getCompression]
    );
};

export default getCompression;

