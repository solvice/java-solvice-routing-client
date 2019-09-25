###############################
#####   CLIENT BUILDER   ######
###############################

# currently we support:
# - angular
# - python
# - java(spring)
# - c#
# - php

# requires installation of swagger-codegen
# mac os: brew install swagger-codegen


SPEC=spec/openapi.yaml
DIR=clients

VERSION=0.9

# it is necessary to use the master snapshot to create a proper R and C# client
SW_VERSION=3.0.8
FILE=swagger-codegen-cli-$SW_VERSION.jar

NAME=routing-client
GROUP=io.solvice


if [[ ! -s $FILE ]]; then
  wget http://repo1.maven.org/maven2/io/swagger/codegen/v3/swagger-codegen-cli/$SW_VERSION/$FILE -O $FILE
  if [[ ! -s $FILE ]]; then
    curl http://repo1.maven.org/maven2/io/swagger/codegen/v3/swagger-codegen-cli/$SW_VERSION/$FILE -O $FILE
  fi
fi


file_size_kb=$(du -k "$FILE" | cut -f1)
if [[ $file_size_kb -lt 1000 ]]; then
  echo corrupt file $FILE, remove it, ensure host exists and try again
  exit
fi

function create {
  LANG=$1
  CONFIG=""
  ADD_PARAMS=""

  case "$LANG" in
	java)
		PKG="io.solvice.routing.api.client"
		CONFIG="--artifact-version $VERSION --api-package $PKG.api --invoker-package $PKG --model-package $PKG.model --artifact-id $NAME --group-id $GROUP --library okhttp-gson -DhideGenerationTimestamp=true"
		;;
	ruby)
		CONFIG="-DgemName=$NAME -DmoduleName=SolviceRoutingClient -DgemVersion=$VERSION"
		;;
	go)
		# CONFIG="-t modules/swagger-codegen/src/main/resources/go"
		ADD_PARAMS="-DpackageName=solvice"
		;;
	swift)
		CONFIG="-DprojectName=SolviceRoutingClient"
		;;
	javascript)
		CONFIG="-t modules/swagger-codegen/src/main/resources/Javascript"
		;;
	haskell)
		;;
	r)
		ADD_PARAMS="-DpackageName=SolviceRoutingClient"
		;;
	php)
		CONFIG="--artifact-version $VERSION --git-repo-id $NAME --git-user-id solvice --api-package $NAME"
		;;
	csharp)
		VER=$(echo $VERSION | cut -d'-' -f 1)
		ADD_PARAMS="-DpackageName=SolviceRoutingClient,packageVersion=$VER"
		;;
  	*)
		;;
  esac


  # echo "create $LANG, config: $CONFIG, additional params: $ADD_PARAMS"
  SH="java -jar $FILE generate -i $SPEC -l $LANG $CONFIG -o $DIR/$LANG $ADD_PARAMS"
  echo $SH
  $SH
}

LANG=$1
if [[ "$LANG" != "" ]]; then
  create $LANG
  exit 0
else
  echo "creating all"

  # the JS client is just too large and not recommended so use nodejs-server
  # create javascript -> nodejs-server

#  create csharp
#  create go
  create java
#  create nodejs-server
#  create php
#  create python
fi
