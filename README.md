# k8s_infra
```
       | x.x.x.x グローバルIP
+------V-------+
| topi-gateway | # 踏み台 
+--------------+
       | 100.x.x.x
+------V--------+ +---------------+ +--------------
| topi-server00 | | topi-server01 | | topi-datastore...
+------|--------+ +-------|-------+ +--------|-----
       +------------------+------------------+-----
```
## 現環境(2023/10/25)
- topi-gateway (XserverVPS / 2G)
- topi-server00 (k3s / 8G) .80
- topi-server01 (k3s / 2G) .81
- topi-datastore (nfs,db / k3s / 2G) .70


## 踏み台(レンタル鯖、クラウド等。グローバルIP持ち)
- `Global IP` : グローバルIP。DNS-Aレコードでドメインに設定する
- `Private IP` : 転送先IP。k8sクラスタのマスターノードのtailscale IP
```
iptables -t nat -A PREROUTING -d << Global IP >>> -j DNAT --to-destination <<< Private IP >>
iptables -t nat -A POSTROUTING -j MASQUERADE
```

## k8s-Cluster
### OS setting
[topi_banana/serversetting-cheatsheet.md (GithubGist)](https://gist.github.com/topi-banana/1916956b9c54af544dc576d3fe159e0b)
### k3s install
Quick-Start Guide [https://docs.k3s.io/quick-start](https://docs.k3s.io/quick-start)
- ~~[--flannel-backend=wireguard-native](https://github.com/k3s-io/k3s/issues/6255#issuecomment-1278872178)~~
- [--disable=traefik](https://docs.k3s.io/networking#:~:text=servers%20with%20the-,%2D%2Ddisable%3Dtraefik,-flag.)

```sh
curl -sfL https://get.k3s.io | sh -s - server \
 --docker \
 --token=topi \
 --disable=traefik \
 --write-kubeconfig-mode=644 \
 --datastore-endpoint="mysql://k3s:k3s@tcp(topi-datastore)/k3s" \
 #--flannel-backend=wireguard-native \
 #--node-ip=$TAILSCALE_IP_NODE \
 #--advertise-address=$TAILSCALE_IP_NODE \
 #--node-external-ip=$EXTERNAL_IP_NODE
```
```
curl -sfL https://get.k3s.io | sh -s - agent \
 --server https://topi-master:6443 \
 --docker \
 --token=topi \
```


## manifests
- [MetalLB (LoadBalancer)](https://metallb.universe.tf/installation/#installation-by-manifest)
- ~~[Calico (CNI)](https://github.com/projectcalico/calico/blob/v3.26.3/manifests/calico.yaml)~~
- [ArgoCD (GitOps)](https://argo-cd.readthedocs.io/en/stable/getting_started)
- [ArgoCD ingress](https://raw.githubusercontent.com/topi-banana/k8s_infra/main/manifests/argocd-ingress.yaml)
- [KEDA (ScaledObject)](https://keda.sh/docs/2.11/deploy/#yaml)
- [Reloader](https://github.com/stakater/Reloader#deploying-to-kubernetes)
- [ingress-nginx (ingress)](https://github.com/kubernetes/ingress-nginx/blob/main/docs/deploy)
- [cert-manager (ingress SSL)](https://cert-manager.io/docs/installation/kubectl)
- [SMB CSI (StorageClass)](https://cloud.google.com/kubernetes-engine/docs/how-to/access-smb-volume?hl=ja)
- ~~[rook/Ceph (Storage,PV/PVC)](https://github.com/rook/rook)~~

## reference
- ~~[K3s multi-node install - TIGERA](https://docs.tigera.io/calico/latest/getting-started/kubernetes/k3s/multi-node-install)~~
- [Kubernetesクラスターを「クラウド↔自宅ネットワーク」間で作る（Tailscale編） - Quitta](https://qiita.com/showchan33/items/7500bcb73b10be437e49)
- [Kubernetes クラスタに Argo CD をインストールして動かす - Zenn](https://zenn.dev/kou_pg_0131/articles/argocd-getting-started)
- [Kubernetesのconfigmapやsecret更新時にワークロードをアップグレードしてくれるReloaderを触ってみた - Quitta](https://qiita.com/asmg07/items/b8e699bc30e5c16b2022)
- [GiganticMinecraft k8s_manifests - Github](https://github.com/GiganticMinecraft/seichi_infra/tree/main/seichi-onp-k8s/manifests/seichi-kubernetes/app-templates/minecraft-gateway-bungeecord)
- ~~[NFSサーバをKubernetesのServiceで作り、ReadWriteManyなPersistentVolumeを作る - Quitta(nfs)](https://qiita.com/showchan33/items/fa3dadc546d4ae5e8c09)~~
- ~~└--> [Deploying NFS Server in Kubernetes - Github](https://github.com/appscode/third-party-tools/tree/master/storage/nfs)~~
- ~~└-->[ftp-kube - Github](https://github.com/latonaio/ftp-kube)~~
- ~~└-->[お試し CephFS - Zenn](https://zenn.dev/t_ume/articles/adedeb6e7bd7ce)~~
- ~~└-->[Quickstart - Rook Ceph Documentation](https://rook.github.io/docs/rook/v1.12/Getting-Started/quickstart/)~~
- [【k8s】ingressがapplyできない。(InternalError) - Qitta](https://qiita.com/magisystem0408/items/48bca4496962fd508556)
