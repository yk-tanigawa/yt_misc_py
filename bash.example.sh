#!/bin/bash
set -beEuo pipefail

PROGNAME=$(basename $(readlink -f $0))
VERSION="1.0"
NUM_POS_ARGS=1

# parse
usage () {
   echo "Usage: $PROGNAME [OPTIONS] FILE"
   echo "$PROGNAME (version $VERSION)"
}

declare -a params=()
for OPT in "$@" ; do
    case "$OPT" in 
        '-h' | '--help' )
            usage >&2 ; exit 1 ; 
            ;;
        '-v' | '--version' )
            echo $VERSION ; exit 0 ;
            ;;
        '-a' )
            FLAG_A=1
            shift 1
            ;;
        '--'|'-' )
            shift 1
            params+=( "$@" )
            break
            ;;
        -*)
            echo "$PROGNAME: illegal option -- '$(echo $1 | sed 's/^-*//')'" 1>&2 ; exit 1
            ;;
        *)
            if [[ ! -z "$1" ]] && [[ ! "$1" =~ ^-+ ]]; then
                params+=( "$1" )
                shift 1
            fi
            ;;
    esac
done
if [ ${#params[@]} -lt ${NUM_POS_ARGS} ]; then
    echo "${NUM_POS_ARGS} positional arguments are required" >&2
    usage >&2 ; exit 1 ; 
fi

if [ "$FLAG_A" ]; then
    echo "Option -a specified."
fi

echo ${params[@]}
echo ${#params[@]}

