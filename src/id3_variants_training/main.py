from .ID3_Class import ID3
import argparse
from pkg_resources import resource_filename
import config

default_file_path = resource_filename(config.__name__, 'config.json')

parser = argparse.ArgumentParser()
parser.add_argument('--config_file', help='Path to the config file that contains variant ranges in JSON format',
                    default=default_file_path)
parser.add_argument('--use_server_vcf_files', action='store_true', default=False,
                    help='Query VCF files from the server')
args = parser.parse_args()

# Creates ID3 object with a path to the config file and whether to use local VCF files or server VCF files
use_local_vcf_files = not args.use_server_vcf_files
id3_obj = ID3(args.config_file, use_local_vcf_files)

# prints the ID3 tree as `tree.png`
id3_obj.print_tree('tree')

# prints the list of all the variant names
print(id3_obj.api.variant_name_list)

# predicts ancestry of the person with the variant `22:50121766:50121767` and no other variant in `variant_name_list`
id3_obj.predict(['22:50121766:50121767'])
