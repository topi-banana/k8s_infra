# k8s_infra

## k3s install
Quick-Start Guide [https://docs.k3s.io/quick-start](https://docs.k3s.io/quick-start)
### 事前準備
#### 別で
- DB* (MariaDB,MySQL,etc...)

pass: `k3s`

user: `k3s`

db_name: `k3s`

- NAS (nfs,ftp,etc...)

k8s pv/pvc用
#### 各ノードに
- tailscale
プライベートネットワーク
- docker
コンテナランタイム

[topi_banana/serversetting-cheatsheet.md (GithubGist)](https://gist.github.com/topi-banana/1916956b9c54af544dc576d3fe159e0b)

```
# tailscale 内のIPで
export DB_ENDPOINT="mysql://k3s:k3s@tcp(xxx.xxx.xxx)/k3s"

# このノードの tailscale IP
export TAILSCALE_IP_NODE=$(tailscale ip -4)

# ホームネットワーク等、アクセスに使うIP
export EXTERNAL_IP_NODE="192.168.xxx.xxx"

curl -sfL https://get.k3s.io | sh -s - server \
 --docker \
 --token=topi \
 --flannel-backend=wireguard-native \
 --no-deploy=traefik \
 --write-kubeconfig-mode=644 \
 --datastore-endpoint=$DB_ENDPOINT \
 --node-ip=$TAILSCALE_IP_NODE \
 --node-external-ip=$EXTERNAL_IP_NODE \
 --advertise-address=$TAILSCALE_IP_NODE
```



## manifests
- ~~[MetalLB (LoadBalancer)](https://metallb.universe.tf/installation/#installation-by-manifest)~~
- [Calico (CNI)](https://docs.tigera.io/calico/latest/getting-started/kubernetes/quickstart)
- [ArgoCD (GitOps)](https://argo-cd.readthedocs.io/en/stable/getting_started)
- [ArgoCD ingress](https://raw.githubusercontent.com/topi-banana/k8s_infra/main/manifests/argocd-ingress.yaml)
- [KEDA (ScaledObject)](https://keda.sh/docs/2.11/deploy/#yaml)
- [Reloader](https://github.com/stakater/Reloader#deploying-to-kubernetes)
- [ingress-nginx (ingress)](https://github.com/kubernetes/ingress-nginx/blob/main/docs/deploy)

## reference
- [Kubernetesクラスターを「クラウド↔自宅ネットワーク」間で作る（Tailscale編） - Quitta](https://qiita.com/showchan33/items/7500bcb73b10be437e49)
- [Kubernetes クラスタに Argo CD をインストールして動かす - Zenn](https://zenn.dev/kou_pg_0131/articles/argocd-getting-started)
- [Kubernetesのconfigmapやsecret更新時にワークロードをアップグレードしてくれるReloaderを触ってみた - Quitta](https://qiita.com/asmg07/items/b8e699bc30e5c16b2022)
- [GiganticMinecraft k8s_manifests - Github](https://github.com/GiganticMinecraft/seichi_infra/tree/main/seichi-onp-k8s/manifests/seichi-kubernetes/app-templates/minecraft-gateway-bungeecord)
- ~~[NFSサーバをKubernetesのServiceで作り、ReadWriteManyなPersistentVolumeを作る - Quitta(nfs)](https://qiita.com/showchan33/items/fa3dadc546d4ae5e8c09)~~
- └--> [Deploying NFS Server in Kubernetes - Github](https://github.com/appscode/third-party-tools/tree/master/storage/nfs)
- ~~└-->[ftp-kube - Github](https://github.com/latonaio/ftp-kube)~~
