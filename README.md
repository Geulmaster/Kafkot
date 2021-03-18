# Kafkot

create configuration.ini file:

![Image of configuration.ini](https://github.com/Geulmaster/Kafkot/blob/main/config/configuration_example.png)

Run helm chart:

`docker login`

`cd ~/.docker`

`kubectl create secret generic regcred \
    --from-file=.dockerconfigjson=config.json \
    --type=kubernetes.io/dockerconfigjson`

In helm_chart/values.yaml make sure that:

`imagePullSecrets:
  - name: regcred`

Finally:

`helm install kafkot helm_chart/`

