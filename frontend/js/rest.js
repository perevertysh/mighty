window.axios = require('axios');
const instance = axios.create({
    baseURL: '/api/'
});

const target = {};
const handler = {
    get(target, name) {
        name = name.replace(/__/g, "/");
        return Object.assign({},
            [
                'get',
                'delete',
                'options',
                'head'
            ].reduce(
                (o, method) => Object.assign({}, o, {
                    [method](url = '', params = {}) {
                        if (typeof url === 'object') {
                            params = url;
                            url = '';
                        }

                        if (url[0] !== '/') {
                            url = '/' + url;
                        }

                        if (url[url.length - 1] !== '/') {
                            url += '/';
                        }
                        let responseType = _.get(params, 'responseType', null)
                        let headers =_.get(params, 'headers', null)
                        return instance[method](name + url, {
                                    responseType,
                                    headers,
                                    params
                                }
                            
                        );
                    }
                }), {}),
            [
                'post',
                'put',
                'patch'
            ].reduce(
                (o, method) => Object.assign({}, o, {
                    [method](url = '', body = {}, params = {}) {
                        if (typeof url === 'object') {
                            params = body;
                            body = url;
                            url = '';
                        }
                        if (url[0] !== '/') {
                            url = '/' + url;
                        }
                        
                        if (url[url.length - 1] !== '/') {
                            url += '/';
                        }
                        let responseType = _.get(params, 'responseType', null)
                        let headers = _.get(params, 'headers', null)
                        return instance[method](name + url, body, {
                                responseType,
                                headers,
                                params
                        });
                    }
                }), {})
        );
    }
};

export default new Proxy(target, handler);