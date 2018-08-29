import requests
import sys
import yaml
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-s', action='store_true')
parser.add_argument('file', metavar='FILE', type=argparse.FileType('r'))


class App:
    def run(self, args):
        self.args = parser.parse_args(args[1:])
        with(self.args.file) as f:
            try:
                reqdata = yaml.load(f)
                #print(reqdata)
                self.run_req(reqdata)
            except Exception as e:
                print(e)
                raise
        #print(args)

    def run_req(self, reqdata):
        response = requests.request(str(reqdata['method']).lower(), reqdata['url'], params=reqdata['params'], headers=reqdata['headers'], data=reqdata['body'])
        if self.args.s:
            print(response.status_code)
        #print(response.text)



def main():
    App().run(sys.argv)
