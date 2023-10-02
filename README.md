# k8s_infra

## k3s install
Quick-Start Guide [https://docs.k3s.io/quick-start](https://docs.k3s.io/quick-start)

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
